# Generated by Django 2.0.2 on 2018-08-01 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0009_walletaddress_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='display',
            field=models.BooleanField(default=False, help_text='Show/Hide this coin anytime'),
        ),
    ]
