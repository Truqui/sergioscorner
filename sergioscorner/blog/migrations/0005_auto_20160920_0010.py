# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 00:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160920_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
