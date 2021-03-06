# Generated by Django 2.0.2 on 2018-07-25 10:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('merchant_tools', '0014_multipayment_payment_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='multipayment',
            name='paid_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='multipayment',
            name='recieved_amount',
            field=models.CharField(default=0, max_length=512),
        ),
        migrations.AddField(
            model_name='multipayment',
            name='recieved_usd',
            field=models.CharField(default=0, max_length=512),
        ),
    ]
