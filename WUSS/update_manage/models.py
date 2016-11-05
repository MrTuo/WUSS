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
