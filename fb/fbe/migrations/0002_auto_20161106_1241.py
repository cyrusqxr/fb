# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-06 04:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fbe', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invitation',
            old_name='acceptemail',
            new_name='accept_email',
        ),
    ]