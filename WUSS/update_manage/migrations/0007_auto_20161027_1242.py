# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-27 04:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('update_manage', '0006_auto_20161026_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rssitem',
            name='url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='url_manage.Urls'),
        ),
    ]
