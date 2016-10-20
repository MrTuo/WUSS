from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

class WUSSUser(models.Model):
    user = models.OneToOneField(User)
    url = models.CharField(max_length=199)
    def __str__(self):
		return self.user.username
