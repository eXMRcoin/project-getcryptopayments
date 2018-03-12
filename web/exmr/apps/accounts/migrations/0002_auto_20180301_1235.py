# Generated by Django 2.0.2 on 2018-03-01 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='buyer_or_seller',
            field=models.PositiveSmallIntegerField(default=0, verbose_name=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Buyer'), (1, 'Seller')], default=0, verbose_name='user type'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='left_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='left by'),
        ),
    ]