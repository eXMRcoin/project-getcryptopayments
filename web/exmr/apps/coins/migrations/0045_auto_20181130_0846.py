# Generated by Django 2.0.2 on 2018-11-30 08:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0044_auto_20181129_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paybyname',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 30, 8, 46, 44, 933882, tzinfo=utc)),
        ),
    ]
