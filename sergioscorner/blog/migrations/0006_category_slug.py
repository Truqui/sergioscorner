# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 23:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160920_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='slug'),
            preserve_default=False,
        ),
    ]