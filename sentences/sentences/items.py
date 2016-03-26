# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from kanjisite.manageset.models import Sentence

class SentenceItem(DjangoItem):
    django_model = Sentence