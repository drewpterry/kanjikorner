#execute this in django shell: execfile('xmltodict/jisho_scraper/jlpt_words_import.py')
import json
from manageset.models import UserProfile, Sets, Words, Kanji
from pprint import pprint
import requests
from bs4 import BeautifulSoup
import csv
import sys

with open('jlpt_level_export2.csv','r') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    count = 0
    for row in reader:
        print row[1], row[2], row[11], count
        # # print count, row[0]
        #
        count = count +1
        if row[1] != "none" and row[0] != "id" and count >75988:
            # encoded_word = row[2].decode('utf-8')
            # print row[2], type(int(row[4]))
            word = Words.objects.filter(real_word = row[1], meaning = row[2])
            # word = Words.objects.get(id = row[0])
            # word.jlpt_level = row[1]
            # print row[1], "hello"
            for each in word:

                # if row[1] == "n/a":
 #
 #                    each.jlpt_level = 7
 #                elif row[1] == "error":
 #                    each.jlpt_level = 6
 #                else:
 #                    each.jlpt_level = row[1]
                 each.jlpt_level = row[11]


                 each.save()
                 # print count, row[0], each.jlpt_level
        # word = Words.objects.get(row)
#         print row
    