# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2020-05-08 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passenger', '0004_auto_20200507_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registermodel',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]