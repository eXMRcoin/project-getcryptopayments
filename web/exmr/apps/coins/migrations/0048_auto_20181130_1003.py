# Generated by Django 2.0.2 on 2018-11-30 10:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0047_auto_20181130_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paybyname',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 30, 10, 3, 13, 683583, tzinfo=utc)),
        ),
    ]
