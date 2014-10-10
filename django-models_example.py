# -*- coding: utf-8 -*-
from django.db import models
from manageset.models import UserProfile, Sets, Words, Kanji

from manageset.models import Knight
# execfile('django-models_example.py')


kanjis = Kanji.objects.all()
wordses =  Words.objects.all()
# UserProfile.objects.all()
# Sets.objects.all()
#
#
# Kanji.objects.filter(id = 1)
# Kanji(kanji_name = name, ect).save()
# Words(real_word = "寒い", meaning = "cold", hiragana = "さむい" , frequency = 3, kanji = 4).save()
# Entry.objects.filter(name='name', title='title').exists()
UserProfile.objects.get(id = 8).known_kanji.filter(id = 8).exists()
# Words.objects.get(meaning = "cold").kanji.add(Kanji.objects.get(pk =4))

# gets me id, need to loop through though to extract full list, change get to all
# next figure out how to return words with kanji associated
UserProfile.objects.get(id = 8).known_kanji.get(id =1).id

WHERE real_word SIMILAR TO '%(本|日)%'
http://stackoverflow.com/questions/22848046/mysql-return-all-rows-where-a-column-contains-any-but-only-keywords-from-a-set


# Get blogs entries with id 1, 4 and 7
>>> Blog.objects.filter(pk__in=[1,4,7])

# for kanji in Kanji.objects.all():
def kanji_match():
    match = 0
    for word in wordses:
        word_test = str(word)
        for single_kanji in kanjis:
            single_kanji_test = str(single_kanji)
            if word_test.find(single_kanji_test) != -1:
                match = match + 1
                print Words.objects.get(pk = word.pk).pk, word, single_kanji
                # print Words.objects.get(id = word.id) #.kanji.add(Kanji.objects.get(kanji_name = single_kanji)).save()
                # Words.objects.get(id = word.id).kanji.add(Kanji.objects.get(kanji_name = single_kanji)).save()
                Words.objects.get(pk = word.pk).kanji.add(Kanji.objects.get(pk = single_kanji.pk))
                # word.kanji.add(single_kanji).save()
                # return # print "false"
            
                
    print match                
                
kanji_match()                