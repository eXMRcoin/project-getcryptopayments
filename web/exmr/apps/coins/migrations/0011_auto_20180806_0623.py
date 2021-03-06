# Generated by Django 2.0.2 on 2018-08-06 06:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0010_coin_display'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phase', models.CharField(max_length=128, verbose_name='Voting_phase')),
                ('time_start', models.DateField()),
                ('time_stop', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='WinnerCoins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phase_name', models.CharField(max_length=64, unique=True)),
                ('winner_coins', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coins.NewCoin', verbose_name='coin')),
            ],
        ),
        migrations.AlterField(
            model_name='coinvote',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
