# Generated by Django 2.0.2 on 2018-09-25 07:17

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0016_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='API',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_question', models.CharField(max_length=512)),
                ('api_answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='InformationalSidebar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inform_topic', models.CharField(max_length=64)),
                ('inform_answer', ckeditor_uploader.fields.RichTextUploadingField()),
                ('order_index', models.IntegerField()),
                ('slug', models.SlugField(default='djangodbmodelsfieldscharfield')),
            ],
        ),
        migrations.CreateModel(
            name='ReceivingSidebar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receive_topic', models.CharField(max_length=64)),
                ('receive_answer', ckeditor_uploader.fields.RichTextUploadingField()),
                ('order_index', models.IntegerField()),
                ('slug', models.SlugField(default='djangodbmodelsfieldscharfield')),
            ],
        ),
    ]
