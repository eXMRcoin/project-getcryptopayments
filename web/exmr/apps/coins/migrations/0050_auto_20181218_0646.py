# Generated by Django 2.0.2 on 2018-12-18 06:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0049_auto_20181218_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paybyname',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 18, 6, 46, 0, 300465, tzinfo=utc)),
        ),
    ]
