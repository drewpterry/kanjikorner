import json
from manageset.models import UserProfile, Sets, Words, Kanji
from pprint import pprint


with open('frequency_lists/wiki_kanji_scrape.json') as data_file:    
    data = json.load(data_file)
    total_count = 0
    kanji_exist_count = 0
    for i in range(0,len(data)):
        total_count += 1
        gradenumber = int(data[i]["grade"])
        kanji_exists = Kanji.objects.filter(kanji_name = data[i]["kanji"],readings = data[i]["readings"], kanji_meaning = data[i]["meaning"], strokes = data[i]["strokes"], grade = gradenumber).exists()
        if kanji_exists:
            the_kanji = Kanji.objects.get(kanji_name = data[i]["kanji"],readings = data[i]["readings"], kanji_meaning = data[i]["meaning"], strokes = data[i]["strokes"], grade = gradenumber)
            kanji_exist_count = kanji_exist_count + 1
            
    print kanji_exist_count,"  ", total_count        
        # Kanji(kanji_name = data[i]["kanji"],readings = data[i]["readings"], kanji_meaning = data[i]["meaning"], strokes = data[i]["strokes"], grade = gradenumber).save()
# print data
        