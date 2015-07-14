# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq_sys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='date',
            field=models.TimeField(auto_now=True),
        ),
    ]
