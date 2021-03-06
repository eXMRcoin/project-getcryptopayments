# Generated by Django 2.0.2 on 2018-05-14 13:24

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0010_helpsidebar_help_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='LegalSidebar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legal_topic', models.CharField(max_length=64)),
                ('legal_answer', ckeditor_uploader.fields.RichTextUploadingField()),
                ('order_index', models.IntegerField()),
                ('slug', models.SlugField(default='djangodbmodelsfieldscharfield')),
            ],
        ),
    ]
