# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-26 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_manage', '0005_urls_track_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='last_check_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='urls',
            name='push_status',
            field=models.BooleanField(default=0),
        ),
    ]