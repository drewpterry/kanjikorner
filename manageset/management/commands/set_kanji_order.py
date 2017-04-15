# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from manageset.models import Kanji, Words, Sets
import csv
import sys
import os
print os.path.dirname(os.path.abspath(__file__))
class Command(BaseCommand):
    help = 'Upload kanji order from words'

    def _upload_kanji_order(self):

        self._clear_kanji_order_from_words()
        kanji_arr = []
        count = 0
        sets = Sets.objects.exclude(master_order = None).order_by("master_order")

        for each_set in sets:
            for word in each_set.words.all():
                for kanji in  word.kanji.all():
                    if kanji not in kanji_arr:
                        count += 1
                        print count
                        kanji_arr.append(kanji)
                        kanji.order_from_words = count 
                        kanji.save()
        return

    def _clear_kanji_order_from_words(self):
        Kanji.objects.all().update(order_from_words=None)

    def handle(self, *args, **options):
        self._upload_kanji_order()       
