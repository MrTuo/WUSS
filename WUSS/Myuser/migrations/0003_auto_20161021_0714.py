# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myuser', '0002_auto_20161021_0712'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='password',
            field=models.CharField(default=1, max_length=14),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='user',
            field=models.CharField(max_length=199),
        ),
    ]
