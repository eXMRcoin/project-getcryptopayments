# Generated by Django 2.0.2 on 2018-12-19 05:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0062_auto_20181218_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paybyname',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 19, 5, 38, 55, 539607, tzinfo=utc)),
        ),
    ]
