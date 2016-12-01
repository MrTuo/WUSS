# coding=utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test, login_required
import feedparser as fp
import datetime
from dateutil.parser import parse
import pytz
from Myuser.models import MyUser
from django.contrib.auth.models import User
from url_manage.models import Urls
from update_manage.models import RssItem, SpiderItem
from django.core.mail import send_mail, EmailMessage
from django.template import loader
from django.utils import timezone
from WUSS.settings import TIME_ZONE, EMAIL_HOST_USER
import urllib.request
from bs4 import BeautifulSoup


# Create your views here.\
def check_update(user):
    urls = Urls.objects.filter(user=user, track_status=1)
    if urls:
        for url in urls:
            if url.last_check_time + datetime.timedelta(url.update_fq) <= timezone.now():  # 到达更新时间
                if url.type == 0:  # RSS訂閱判斷
                    get_RSS_item(url)  # 记录RSS中所有item更新
                else:  # 一般URL訂閱判斷
                    get_spider_item(url)

        send_update_email(user)  # 向用户发送更新邮件


def get_RSS_item(url):
    '''
    将RSS中更新内容保存
    :param url:RSSurl
    :return:
    '''
    now = timezone.now()
    is_update = 0  # 记录是否有内容更新
    if url.track_status:
        rss = fp.parse(url.url)
        items = rss.entries
        is_delete_origin_items = 0  # 是否已删除原有item
        for item in items:
            pubTime = parse(item.published).replace(tzinfo=pytz.timezone(TIME_ZONE))
            last_check_time = parse(url.last_check_time.strftime("%Y %m %d %H:%M:%S")).replace(
                tzinfo=pytz.timezone(TIME_ZONE))
            if pubTime > last_check_time:  # 发布时间大于更新时间
                is_update = 1
                if not is_delete_origin_items:
                    RssItem.objects.filter(url=url).delete()  # 删除url所有原有的item
                    is_delete_origin_items = 1
                # 保存新的item到url
                title = item.title
                link = item.link
                author = item.author
                description = item.description
                new_item = RssItem(
                    title=title,
                    link=link,
                    pubDate=pubTime,
                    author=author,
                    description=description,
                    url=url
                )
                new_item.save()
            else:
                pass
                # 未更新的item
        if is_update:
            Urls.objects.filter(id=url.id).update(push_status=1, last_check_time=now)  # 修改推送状态为1,上次检查时间为当前时间
        else:
            pass  # 无有推送内容
    else:
        # 该url状态为未跟踪
        pass


def get_spider_item(url):
    '''
    一般url更新訂閱判斷（採用爬蟲）
    :param url:
    :return:
    '''
    if url.track_status:
        rq = urllib.request.Request(url.url)
        rq.add_header("user-agent", "Mozilla/5.0")  # 伪装浏览器
        response1 = urllib.request.urlopen(rq)
        html_content = response1.read()  # 获取页面html信息

        soup = BeautifulSoup(html_content, 'lxml')  # 创建bs对象处理html页面
        items = SpiderItem.objects.filter(url=url)# 获取当前页面用户选取的所有标签对象
        for item in items:# 比较每一个标签对象是否发生更新
            attr_dic = get_attr_dic(item.attr_str)# 创建标签属性键值对
            tag_name = attr_dic['tag'] # 获取标签名称
            del attr_dic['tag'] # 删除标签名称键值对
            target = soup.find_all(tag_name, attrs=attr_dic)# 根据标签属性键值定位到标签
            if target: # target中有元素
                target=target[0]
                new_content = ""# 保存新爬取下来的内容
                for string in target.stripped_strings:# 将target标签中所有文字信息提取并保存到new_content中
                    new_content += string + "\n"
                pass
            else: # target中无元素，说明页面发生改变，用户需要重新选择区域。
                item.has_changed = True


    pass


def send_update_email(user):
    '''
    將需要推送的內容一并推送給用戶
    :param user:
    :return:
    '''
    urls = Urls.objects.filter(user=user, push_status=1)
    if urls:
        dic_urls = []
        context = {}
        for url in urls:
            dic_url = {}
            dic_url['last_check_time'] = url.last_check_time
            dic_url['title'] = url.title
            dic_url['items'] = RssItem.objects.filter(url=url)
            dic_urls.append(dic_url)
        context['urls'] = dic_urls
        context['username'] = user.username
        html_content = loader.render_to_string(
            'send_email_template.html',
            context,
        )
        subject = "WUSS订阅更新"
        msg = EmailMessage(
            subject,
            html_content,
            EMAIL_HOST_USER,
            [user.email],
        )
        msg.content_subtype = "html"
        print("---send_mail---", timezone.now())
        print("user:", user.username, "urls:")
        for url in urls:
            print(url.url)
        try:
            msg.send()
            print("success!")

        except Exception as e:
            print(e)
        urls.update(push_status=0)  # 将推送状态设置为0


def check_all_update():
    '''
    检查所有用户的更新，并进行实时推送。后续考虑采用多线程进行优化
    :return:
    '''
    while 1:
        users = User.objects.all()
        for user in users:
            check_update(user)


def get_attr_dic(attr_str):
    '''
    根据attr_str串获取标签属性键值对
    :param attr_str:
    :return:
    '''
    attr_dic = {}
    arr = attr_str.split(',')
    for a in arr:
        arr2 = a.split(':')
        attr_dic[arr2[0]] = arr2[1]
    return attr_dic
