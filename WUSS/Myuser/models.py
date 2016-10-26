# coding=utf-8
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

class MyUser(models.Model):
    user = models.OneToOneField(User)
    #url = models.CharField(max_length=199)
