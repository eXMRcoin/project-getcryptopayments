# Generated by Django 2.0.2 on 2018-10-10 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchant_tools', '0031_buttoninvoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buttoninvoice',
            name='buyer_note',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
