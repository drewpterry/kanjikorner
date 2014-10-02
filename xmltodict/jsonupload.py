import json
from manageset.models import UserProfile, Sets, Words, Kanji
from pprint import pprint


with open('items.json') as data_file:    
    data = json.load(data_file)
    for i in range(0,len(data)):
        gradenumber = int(data[i]["grade"])
        Kanji(kanji_name = data[i]["kanji"],readings = data[i]["readings"], kanji_meaning = data[i]["meaning"], strokes = data[i]["strokes"], grade = gradenumber).save()
# print data
        