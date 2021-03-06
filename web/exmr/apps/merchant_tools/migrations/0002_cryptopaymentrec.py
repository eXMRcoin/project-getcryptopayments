# Generated by Django 2.0.2 on 2018-07-05 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0001_initial'),
        ('merchant_tools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoPaymentRec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_id', models.CharField(max_length=128, verbose_name='merchant id')),
                ('item_name', models.CharField(max_length=128)),
                ('item_amount', models.CharField(max_length=128)),
                ('item_number', models.CharField(max_length=128)),
                ('item_qty', models.CharField(max_length=128)),
                ('invoice_number', models.CharField(max_length=128)),
                ('unique_id', models.CharField(max_length=128)),
                ('tax_amount', models.CharField(max_length=128)),
                ('shipping_cost', models.CharField(max_length=128)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('email_addr', models.CharField(max_length=128)),
                ('addr_l1', models.CharField(max_length=128)),
                ('addr_l2', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('state', models.CharField(max_length=128)),
                ('zipcode', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=128)),
                ('buyer_note', models.BooleanField(default=False)),
                ('selected_coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coins.Coin')),
            ],
        ),
    ]
