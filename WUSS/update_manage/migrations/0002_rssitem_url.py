# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-26 10:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('url_manage', '0002_auto_20161026_1813'),
        ('update_manage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rssitem',
            name='url',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='url_manage.Urls'),
            preserve_default=False,
        ),
    ]
