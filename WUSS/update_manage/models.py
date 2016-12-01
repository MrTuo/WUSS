# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from url_manage.models import Urls


# Create your models here.

class RssItem(models.Model):
    '''
    保存Rss中item标签内的内容
    '''
    title = models.CharField(max_length=150)
    link = models.CharField(max_length=150)
    pubDate = models.DateTimeField()
    author = models.CharField(max_length=100)
    description = models.TextField()
    url = models.ForeignKey(Urls)

    def __unicode__(self):
        return self.title


class SpiderItem(models.Model):
    '''
    保存一般URL中的用户指定标签内容
    '''
    attr_str = models.CharField(max_length=200) # 保存属性键值对
    text_content = models.TextField(blank=True) # 保存最近爬取到的文字信息
    has_changed = models.BooleanField(default=0)# 原网页的这个标签是否已经发生改变，如果发生改变，需要用户到页面重新选取这个标签。
    url = models.ForeignKey(Urls)               # 所属url

    def __str__(self):
        return self.url.title
