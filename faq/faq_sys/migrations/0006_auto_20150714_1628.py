# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('faq_sys', '0005_auto_20150714_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='question',
            name='date_time',
        ),
        migrations.AddField(
            model_name='answer',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 14, 8, 28, 4, 291754, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='time',
            field=models.TimeField(default=datetime.datetime(2015, 7, 14, 8, 28, 7, 3692, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 7, 14, 8, 28, 8, 715633, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='time',
            field=models.TimeField(default=datetime.datetime(2015, 7, 14, 8, 28, 10, 875807, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
