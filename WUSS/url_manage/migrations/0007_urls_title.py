# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-27 06:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_manage', '0006_auto_20161026_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='urls',
            name='title',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
