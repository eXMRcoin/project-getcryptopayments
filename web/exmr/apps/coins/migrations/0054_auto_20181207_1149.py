# Generated by Django 2.0.2 on 2018-12-07 11:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0053_auto_20181206_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paybyname',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 7, 11, 49, 19, 638715, tzinfo=utc)),
        ),
    ]
