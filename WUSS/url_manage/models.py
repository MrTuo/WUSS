# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Urls(models.Model):
    url = models.CharField(max_length = 150)       #url内容
    last_check_time = models.DateTimeField()       #上次推送时间
    update_fq = models.IntegerField(default = 1)   #更新频率
    track_status = models.BooleanField(default = 1)#是否跟踪
    push_status = models.BooleanField(default = 0) #推送状态
   # user = models.ForeignKey(User)                 #所属用户
    title = models.CharField(max_length = 30)      #url名（供推送显示）

    def __unicode__(self):
        return self.url
