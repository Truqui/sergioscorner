# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20160920_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description_tag',
            field=models.CharField(default='Description', max_length=156),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='title_tag',
            field=models.CharField(default='title', max_length=47),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='description_tag',
            field=models.CharField(default='description', max_length=156),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='title_tag',
            field=models.CharField(default='Title', max_length=47),
            preserve_default=False,
        ),
    ]
