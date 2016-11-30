# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from url_manage.models import Urls
# Create your models here.

class RssItem(models.Model):
    '''
    保存Rss中item标签内的内容
    '''
    title = models.CharField(max_length = 150)
    link = models.CharField(max_length = 150)
    pubDate = models.DateTimeField()
    author = models.CharField(max_length = 100)
    description = models.TextField()
    url = models.ForeignKey(Urls)
    def __unicode__(self):
        return self.title

class SpyderItem(models.Model):
    '''
    保存一般URL中的用户指定标签内容
    '''
    tag_name = models.CharField(max_length=100)
    id_name = models.CharField(max_length=100)
    class_name = models.ChrField(max_length=100)
    text_content = models.TextField()
    url = models.ForeignKey(Urls)
    def __unicode__(self):
        return self.url.title


