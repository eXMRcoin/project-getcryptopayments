# Generated by Django 2.0.2 on 2019-04-01 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0085_coin_extra_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Crypto'), (1, 'Ripple'), (2, 'Tokens'), (3, 'Fiat')], default=0, verbose_name='type'),
        ),
    ]
