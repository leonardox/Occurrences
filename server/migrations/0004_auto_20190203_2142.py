# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-02-03 21:42
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AlterField(
            model_name='post',
            name='sumary',
            field=ckeditor.fields.RichTextField(default='New Post'),
        ),
    ]
