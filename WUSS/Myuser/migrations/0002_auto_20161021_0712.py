# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 07:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Myuser', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WUSSUser',
            new_name='MyUser',
        ),
    ]