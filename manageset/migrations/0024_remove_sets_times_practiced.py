# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-02-14 12:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manageset', '0023_auto_20170212_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sets',
            name='times_practiced',
        ),
    ]