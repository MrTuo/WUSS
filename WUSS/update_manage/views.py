from django.shortcuts import render
import feedparser as fp
import datetime
from dateutil.parser import parse
from Myuser.models import *
from url_manage.models import *

# Create your views here.

def get_item(url):
    '''
    输入：RSSurl
    将RSS中更新内容保存
    :param url:
    :return:
    '''
    now = datetime.datetime.now()
    is_update = 0#记录是否有内容更新
    if url.st1:
        rss = fp.parse(url.url_content)
        items = rss.entries
        for item in items:
            pubTime = parse(item.published)
            if pubTime > url.update_time:#发布时间大于更新时间
                is_update = 1
                #删除url所有原有的item
                #保存新的item到url
            else:
                pass
                #未更新的item
        if is_update:
            pass
            #设置url推送状态为1
        else:
            pass#无有推送内容
    else:
        #该url状态为未跟踪
        pass


