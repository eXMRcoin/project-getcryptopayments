# Generated by Django 2.0.2 on 2018-12-31 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0035_auto_20181018_0528'),
    ]

    operations = [
        migrations.AddField(
            model_name='kyc',
            name='ssn',
            field=models.CharField(default='zzzzzzzzzzzzzzzz', max_length=150),
            preserve_default=False,
        ),
    ]
