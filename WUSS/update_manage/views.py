# coding=utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test, login_required
import feedparser as fp
import datetime
from dateutil.parser import parse
from Myuser.models import *
from url_manage.models import *
from update_manage.models import *

# Create your views here.\
@login_required
def check_update(req):
    urls = Urls.objects.filter(user = req.user)
    for url in urls:
        get_item(url)
    return HttpResponse('hello!')

def get_item(url):
    '''
    输入：RSSurl
    将RSS中更新内容保存
    :param url:
    :return:
    '''
    now = datetime.datetime.now()
    is_update = 0#记录是否有内容更新
    if url.track_status:
        rss = fp.parse(url.url)
        items = rss.entries
        for item in items:
            pubTime = parse(item.published)
            if pubTime > parse(url.last_check_time.strftime("%Y %m %d %H:%M:%S")):#发布时间大于更新时间
                is_update = 1
                is_delete_origin_items = 0#是否已删除原有item
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


