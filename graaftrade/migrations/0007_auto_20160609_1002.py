# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graaftrade', '0006_auto_20160606_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='name',
            field=models.CharField(default='STOCK', max_length=128),
        ),
    ]
