# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-04-02 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageset', '0024_remove_sets_times_practiced'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersets',
            name='test_field',
            field=models.BooleanField(default=False),
        ),
    ]
