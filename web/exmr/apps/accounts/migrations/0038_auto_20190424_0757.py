# Generated by Django 2.0.2 on 2019-04-24 07:57

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0037_profile_refered_by'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Address',
            new_name='Addresses',
        ),
    ]