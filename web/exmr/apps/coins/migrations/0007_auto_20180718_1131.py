# Generated by Django 2.0.2 on 2018-07-18 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0006_auto_20180718_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='copromotion',
            name='urls',
            field=models.ManyToManyField(to='coins.CoPromotionURL', verbose_name='CoPromotion URL'),
        ),
    ]
