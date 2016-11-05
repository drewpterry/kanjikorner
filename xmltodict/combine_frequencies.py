# -*- coding: utf-8 -*-
#execfile('xmltodict/combine_frequencies.py')
from manageset.models import UserProfile, Sets, Words, Kanji, WordMeanings

all_words = Words.objects.all()

count = 0
for each in all_words:
    count = count + 1
    each.combine_frequencies()
    # new_number = count / 1000
 #    new_number = math.floor(new_number)
 #    print new_number
 #    each.frequency_thousand = count
    each.save()
    print count