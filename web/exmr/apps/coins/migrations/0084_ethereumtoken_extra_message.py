# Generated by Django 2.0.2 on 2019-03-26 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0083_auto_20190326_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='ethereumtoken',
            name='extra_message',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
    ]
