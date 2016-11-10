# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.IntegerField(default=0)),
                ('target', models.IntegerField(default=0)),
                ('email', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=100)),
                ('acceptemail', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='oneword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.IntegerField(default=0)),
                ('target', models.IntegerField(default=0)),
                ('oneword', models.CharField(max_length=100)),
            ],
        ),
    ]