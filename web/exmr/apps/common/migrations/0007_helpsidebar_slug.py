# Generated by Django 2.0.2 on 2018-05-14 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_helpsidebar_order_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='helpsidebar',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]