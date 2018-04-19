# Generated by Django 2.0.2 on 2018-04-13 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_auto_20180413_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twofactorsecurity',
            name='two_factor',
            field=models.CharField(blank=True, choices=[(None, 'None'), ('email', 'Email'), ('2fa', 'Linked 2FA Accounts-')], default='email', max_length=20, null=True, verbose_name='2 Factor Authentication'),
        ),
    ]
