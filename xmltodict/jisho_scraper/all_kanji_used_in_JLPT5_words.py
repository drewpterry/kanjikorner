#execute this in django shell: execfile('xmltodict/jisho_scraper/all_kanji_used_in_JLPT5_words.py')
import json
from manageset.models import UserProfile, Sets, Words, Kanji
from pprint import pprint
import csv
import sys


def all_kanji(output_file):
    with open(output_file,'wt') as fp:
        words = Words.objects.filter(jlpt_level__in = [1,2,3,4,5])
        unique_kanji = []
        # print words.count()
        for each in words:
            each =  each.kanji.all()
            for kanji in each:
                if kanji.id not in unique_kanji:
                    unique_kanji.append(kanji.id)
        
        print len(unique_kanji)        
        
        
# all_kanji()      


def jlpt_lvl1_words(output_file):
    with open(output_file,'wt') as fp:
        wr = csv.writer(fp, delimiter=";")
        wr.writerow(['id','word', 'meaning', 'jlpt level'])
        kanji_in = Kanji.objects.filter(jlpt_level = 5).values_list('id', flat = True)
        words = Words.objects.filter(kanji__in = kanji_in, jlpt_level = 5).exclude(published = False).exclude(frequency_thousand = None).exclude(frequency_thousand__gte = 21).order_by('-combined_frequency').prefetch_related('kanji').distinct()[0:1000]
        words_list = list(words)
       
        i = 0
        for each in list(words):

            kanji = each.kanji.all()
            id_list = set()
            for kanji_id in kanji:
                id_list.add(kanji_id.id)


            the_one_list = list(id_list - set(kanji_in))
            print the_one_list

            if the_one_list:
                print "hell0"
                words_list.remove(each)
              
        for each in words_list:
            print each,"got here"
            wr.writerow([each.id, each.real_word.encode('utf-8'), each.jlpt_level])
            fp.flush()
            
            
    print words.count(), "finished"
    
    
jlpt_lvl1_words('jlpt_level1_word_list')    