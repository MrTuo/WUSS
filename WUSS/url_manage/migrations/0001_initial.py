# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-26 01:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='urls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=150)),
                ('last_check_time', models.CharField(max_length=20)),
                ('update_fq', models.IntegerField(default=1)),
                ('push_status', models.BooleanField(default=1)),
                ('user', models.CharField(max_length=10)),
            ],
        ),
    ]
