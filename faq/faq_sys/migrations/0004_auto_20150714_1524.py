# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq_sys', '0003_auto_20150714_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
