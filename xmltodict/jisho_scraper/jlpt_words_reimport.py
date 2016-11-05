#execute this in django shell: execfile('xmltodict/jisho_scraper/jlpt_words_reimport.py')
import json
from manageset.models import UserProfile, Sets, Words, Kanji
from pprint import pprint
import requests
from bs4 import BeautifulSoup
import csv
import sys

with open('jlpt_words2.csv','r') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    count = 0
    Words.objects.all().update(jlpt_level = 7)
    for row in reader:
        count += 1
        # print row[0], row[1], row[2], row[3], row[4], count
        if row[1] == row[2]:
            
            word = Words.objects.filter(real_word = "none", hiragana = row[2])
        else:
            word = Words.objects.filter(real_word = row[1], hiragana = row[2])   
        # word = Words.objects.filter(real_word = "none")
        for each in word:
            print row[0], row[1], row[2], row[3], count
            each.jlpt_level = row[3]
            each.save()

        # count = count +1
#         if row[1] != "none" and row[0] != "id" and count >75988:
#
#             word = Words.objects.filter(real_word = row[1], meaning = row[2])
            
            # for each in word:

                # if row[1] == "n/a":
 #
 #                    each.jlpt_level = 7
 #                elif row[1] == "error":
 #                    each.jlpt_level = 6
 #                else:
 #                    each.jlpt_level = row[1]
                 # each.jlpt_level = row[11]


                 # each.save()
                 # print count, row[0], each.jlpt_level
        # word = Words.objects.get(row)
#         print row
    