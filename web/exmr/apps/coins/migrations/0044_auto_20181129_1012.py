# Generated by Django 2.0.2 on 2018-11-29 10:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0043_auto_20181121_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paybyname',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 29, 10, 12, 23, 85615, tzinfo=utc)),
        ),
    ]
