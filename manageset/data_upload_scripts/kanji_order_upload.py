# -*- coding: utf-8 -*-
from manageset.models import Kanji
import csv
import sys
import os
# print os.path.dirname(os.path.abspath(__file__))
# with open('../data/Kanji/kanji_order', 'r') as csvfile:
# print os.listdir("../data/Kanji/")
with open('kanji_order_NOV6.csv', 'rU') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    row_count = 0
    for row in reader:
        row_count += 1
        if row_count == 1:
            pass
        else:
            kanji = row[2].decode("utf-8")
            kanji = Kanji.objects.get(kanji_name=kanji)
            kanji.master_order = row[0]
            kanji.save()
            print row[0], kanji
    
