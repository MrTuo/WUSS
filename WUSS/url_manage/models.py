# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Urls(models.Model):
    url = models.CharField(max_length = 150)
    last_check_time = models.DateTimeField()
    update_fq = models.IntegerField(default = 1)#
    track_status = models.BooleanField(default = 1)
    push_status = models.BooleanField(default = 0)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.url
