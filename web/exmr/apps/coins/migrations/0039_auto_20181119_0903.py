# Generated by Django 2.0.2 on 2018-11-19 09:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0038_auto_20181115_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='paybynamepurchase',
            name='expiry',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paybyname',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 19, 9, 3, 55, 706068, tzinfo=utc)),
        ),
    ]
