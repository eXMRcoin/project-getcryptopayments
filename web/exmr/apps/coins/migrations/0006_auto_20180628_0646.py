# Generated by Django 2.0.2 on 2018-06-28 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='coin_hosting_type',
            field=models.CharField(choices=[('HOSTED', 'HOSTED'), ('POLONEIX', 'poloneix'), ('BINANCE', 'binance'), ('OKEX', 'okex')], default='HOSTED', max_length=20),
        ),
    ]
