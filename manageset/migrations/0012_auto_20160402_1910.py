# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-02 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageset', '0011_words_scrape_failed'),
    ]

    operations = [
        migrations.AddField(
            model_name='kanji',
            name='aozora_frequency',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='kanji',
            name='news_frequency',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='kanji',
            name='twitter_frequency',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='kanji',
            name='wikipedia_frequency',
            field=models.FloatField(null=True),
        ),
    ]
