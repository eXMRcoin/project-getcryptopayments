# Generated by Django 2.0.2 on 2018-12-20 09:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0066_merge_20181220_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paybyname',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 20, 9, 51, 59, 472908, tzinfo=utc)),
        ),
    ]
