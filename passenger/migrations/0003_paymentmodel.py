# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2020-05-08 02:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
        ('passenger', '0002_auto_20200506_2350'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=500)),
                ('analysis', models.CharField(max_length=500)),
                ('manaid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.UploadModel')),
                ('passid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='passenger.RegisterModel')),
            ],
        ),
    ]