# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-26 11:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('update_manage', '0003_auto_20161026_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rssitem',
            name='url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='url_manage.Urls'),
        ),
    ]
