from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

class MyUser(models.Model):
    user = models.OneToOneField(User)
    url = models.CharField(max_length=199)

class VerificationCode(models.Model):
    email = models.CharField(max_length=50)
    VCode = models.CharField(max_length=6)