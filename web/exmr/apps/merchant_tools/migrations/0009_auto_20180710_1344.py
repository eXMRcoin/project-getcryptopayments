# Generated by Django 2.0.2 on 2018-07-10 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchant_tools', '0008_auto_20180710_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlmaker',
            name='item_desc',
            field=models.CharField(default='', max_length=512),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='urlmaker',
            name='item_name',
            field=models.CharField(max_length=128),
        ),
    ]
