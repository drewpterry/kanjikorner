# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-22 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageset', '0010_sentence_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='words',
            name='scrape_failed',
            field=models.BooleanField(default=False),
        ),
    ]