# Generated by Django 2.0.2 on 2018-05-14 13:05

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_remove_helpsidebar_help_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='helpsidebar',
            name='help_answer',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=1),
            preserve_default=False,
        ),
    ]
