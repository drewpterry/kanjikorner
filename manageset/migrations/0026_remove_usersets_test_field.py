# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-04-02 17:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manageset', '0025_usersets_test_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersets',
            name='test_field',
        ),
    ]