# Generated by Django 2.0.2 on 2018-10-19 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchant_tools', '0035_auto_20181016_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='ButtonItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(max_length=128, unique=True)),
                ('item_name', models.CharField(max_length=128)),
                ('item_amount', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
    ]
