# Generated by Django 2.0.2 on 2018-03-22 06:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180312_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='date_format',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='time_format',
        ),
        migrations.AddField(
            model_name='profile',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date time'),
            preserve_default=False,
        ),
    ]
