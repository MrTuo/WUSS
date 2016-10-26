from django.shortcuts import render
import feedparser as fp
import datetime
from dateutil.parser import parse
from Myuser.models import *
from url_manage.models import *

# Create your views here.

def get_item(url):
    '''
    ���룺RSSurl
    ��RSS�и������ݱ���
    :param url:
    :return:
    '''
    now = datetime.datetime.now()
    is_update = 0#��¼�Ƿ������ݸ���
    if url.st1:
        rss = fp.parse(url.url_content)
        items = rss.entries
        for item in items:
            pubTime = parse(item.published)
            if pubTime > url.update_time:#����ʱ����ڸ���ʱ��
                is_update = 1
                #ɾ��url����ԭ�е�item
                #�����µ�item��url
            else:
                pass
                #δ���µ�item
        if is_update:
            pass
            #����url����״̬Ϊ1
        else:
            pass#������������
    else:
        #��url״̬Ϊδ����
        pass


