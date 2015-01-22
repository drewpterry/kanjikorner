# -*- coding: utf-8 -*-
#execfile('xmltodict/kanji_word_matcher.py')
from django.db import models
from manageset.models import UserProfile, Sets, Words, Kanji



kanjis = Kanji.objects.all()
wordses =  Words.objects.all()







# for kanji in Kanji.objects.all():
def kanji_match():
    match = 0
    for word in wordses:
        word_test = str(word)
        for single_kanji in kanjis:
            single_kanji_test = str(single_kanji)
            if word_test.find(single_kanji_test) != -1:
                
                match = match + 1
                # print word.kanji.all()
                kanji_association_exists =  word.kanji.filter(kanji_name = single_kanji_test).exists()
                
                if not kanji_association_exists:
                    # print kanji_association_exists
                    print kanji_association_exists, word, single_kanji
                    word.kanji.add(single_kanji)
                # print Words.objects.get(pk = word.pk).pk, word, single_kanji
                # print Words.objects.get(id = word.id) #.kanji.add(Kanji.objects.get(kanji_name = single_kanji)).save()
                # Words.objects.get(id = word.id).kanji.add(Kanji.objects.get(kanji_name = single_kanji)).save()
                
                
                # Words.objects.get(pk = word.pk).kanji.add(Kanji.objects.get(pk = single_kanji.pk))
                # word.kanji.add(single_kanji).save()
                # return # print "false"
            
                
    # print match
                
kanji_match()                