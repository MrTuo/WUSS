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
from update_manage.models import RssItem
from django.core.mail import send_mail,EmailMessage
from django.template import loader
from django.utils import timezone
from WUSS.settings import TIME_ZONE, EMAIL_HOST_USER

# Create your views here.\
def check_update(user):
    urls = Urls.objects.filter(user = user,track_status=1)
    if urls:
        for url in urls:
            if url.last_check_time+datetime.timedelta(url.update_fq)<=timezone.now():
                get_item(url)
        send_update_email(user)

def get_item(url):
    '''
    输入：RSSurl
    将RSS中更新内容保存
    :param url:
    :return:
    '''
    now = timezone.now()
    is_update = 0#记录是否有内容更新
    if url.track_status:
        rss = fp.parse(url.url)
        items = rss.entries
        is_delete_origin_items = 0#是否已删除原有item
        for item in items:
            pubTime = parse(item.published).replace(tzinfo=pytz.timezone(TIME_ZONE))
            last_check_time = parse(url.last_check_time.strftime("%Y %m %d %H:%M:%S")).replace(tzinfo=pytz.timezone(TIME_ZONE))
            if pubTime > last_check_time:#发布时间大于更新时间
                is_update = 1
                if not is_delete_origin_items:
                    RssItem.objects.filter(url = url).delete()#删除url所有原有的item
                    is_delete_origin_items = 1
                #保存新的item到url
                title = item.title
                link = item.link
                author = item.author
                description = item.description
                new_item = RssItem(
                    title = title,
                    link = link,
                    pubDate = pubTime,
                    author = author,
                    description = description,
                    url = url
                )
                new_item.save()
            else:
                pass
                #未更新的item
        if is_update:
            Urls.objects.filter(id = url.id).update(push_status = 1, last_check_time = now)#修改推送状态为1,上次检查时间为当前时间
        else:
            pass#无有推送内容
    else:
        #该url状态为未跟踪
        pass

def send_update_email(user):
    urls = Urls.objects.filter(user = user,push_status = 1)
    if urls:
        dic_urls = []
        context={}
        for url in urls:
            dic_url = {}
            dic_url['last_check_time']=url.last_check_time
            dic_url['title'] = url.title
            dic_url['items'] = RssItem.objects.filter(url = url)
            dic_urls.append(dic_url)
        context['urls']=dic_urls
        context['username']=user.username
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
    users = User.objects.all()
    while 1:
        for user in users:
            check_update(user)



