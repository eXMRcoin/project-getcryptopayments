# Generated by Django 2.0.2 on 2018-04-12 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_remove_twofactoraccount_totp'),
    ]

    operations = [
        migrations.AddField(
            model_name='twofactoraccount',
            name='totp',
            field=models.CharField(max_length=128, null=True, verbose_name='Authentication Code'),
        ),
    ]
