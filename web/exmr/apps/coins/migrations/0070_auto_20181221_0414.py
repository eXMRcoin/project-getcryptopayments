# Generated by Django 2.0.2 on 2018-12-21 04:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0069_merge_20181221_0414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paybyname',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 21, 4, 14, 58, 465953, tzinfo=utc)),
        ),
    ]
