# Generated by Django 2.0.2 on 2018-11-15 12:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0037_auto_20181115_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paybyname',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 15, 12, 44, 57, 529942, tzinfo=utc)),
        ),
    ]
