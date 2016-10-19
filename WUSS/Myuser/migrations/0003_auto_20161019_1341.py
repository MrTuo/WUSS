# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Myuser', '0002_auto_20161019_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='user',
            field=models.CharField(max_length=14),
            preserve_default=True,
        ),
    ]
