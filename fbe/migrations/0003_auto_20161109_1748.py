# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-09 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbe', '0002_auto_20161106_1241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitation',
            name='accept_email',
        ),
        migrations.AddField(
            model_name='accept',
            name='accept_email',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accept',
            name='time',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invitation',
            name='time',
            field=models.CharField(default='2016-11-09 00:00:00', max_length=50),
            preserve_default=False,
        ),
    ]
