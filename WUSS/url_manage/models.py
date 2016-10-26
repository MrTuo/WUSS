# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class urls(models.Model):
    url = models.CharField(max_length = 150)
    last_check_time = models.CharField(max_length = 20)
    update_fq = models.IntegerField(default = 1)
    push_status = models.BooleanField(default = 1)
    user = models.CharField(max_length = 10)

    def __unicode__(self):
        return self.url
