# Generated by Django 2.2.17 on 2020-12-18 09:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20201218_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 12, 18, 9, 37, 41, 998997, tzinfo=utc)),
        ),
    ]
