# Generated by Django 2.0.2 on 2018-09-19 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0025_paypaltransaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paypaltransaction',
            name='coin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coins.Coin', verbose_name='coin'),
        ),
    ]
