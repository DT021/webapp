# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graaftrade', '0009_auto_20160609_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock_news',
            name='published',
            field=models.DateTimeField(auto_now_add=True, default='2016-01-01 12:00:00'),
            preserve_default=False,
        ),
    ]
