#execute this in django shell: execfile('xmltodict/all_word_upload.py')
import json
from manageset.models import UserProfile, Sets, Words, Kanji
from pprint import pprint

with open('xmltodict/word_list.json') as data_file:    
    data = json.load(data_file)
    for i in range(0,len(data)):
        Words(real_word = data[i]["full_word"],meaning = data[i]["definitions"][0], hiragana = data[i]["hiragana"], frequency = data[i]["frequency"]).save()
    print data
# print data