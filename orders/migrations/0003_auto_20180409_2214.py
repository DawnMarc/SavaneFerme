# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-09 19:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20180409_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 4, 9, 19, 14, 56, 910683, tzinfo=utc)),
        ),
    ]