# -*- coding: utf-8 -*-
#execfile('xmltodict/add_frequency_thousand.py')
from math import floor, ceil
from manageset.models import UserProfile, Sets, Words, Kanji, WordMeanings

count = 0
all_words = Words.objects.filter(combined_frequency__gte = 1).order_by('-combined_frequency')
for each in all_words:
    count = count + 1
    new_number = count / 1000
    new_number = int(floor(new_number)) + 1
    print new_number
    each.frequency_thousand = new_number
    each.save()
    
    print count