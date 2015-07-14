# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('faq_sys', '0002_auto_20150714_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='date',
        ),
        migrations.RemoveField(
            model_name='question',
            name='date',
        ),
        migrations.AddField(
            model_name='answer',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 14, 7, 22, 43, 862207, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 14, 7, 23, 3, 614848, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
