# Generated by Django 2.0.2 on 2019-01-23 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchant_tools', '0058_simplebuttoninvoice_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simplebuttoninvoice',
            name='payment_status',
            field=models.CharField(default='Null', max_length=256),
            preserve_default=False,
        ),
    ]
