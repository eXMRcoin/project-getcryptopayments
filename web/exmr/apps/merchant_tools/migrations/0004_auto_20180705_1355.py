# Generated by Django 2.0.2 on 2018-07-05 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchant_tools', '0003_cryptopaymentrec_wallet_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptopaymentrec',
            name='buyer_note',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
