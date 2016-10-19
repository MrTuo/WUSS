from django.db import models
from django.contrib.auth.models import User

class MyUser(models.Model):
    user = models.CharField(max_length=14)
    email = models.EmailField()
    password = models.CharField(max_length=14)
