# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq_sys', '0004_auto_20150714_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='date_time',
            field=models.TimeField(auto_now=True),
        ),
    ]
