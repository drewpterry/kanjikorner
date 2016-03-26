
#execfile('xmltodict/jsonupload.py')
import json
from manageset.models import UserProfile, Sets, Words, Kanji
from pprint import pprint



with open('xmltodict/frequency_lists/wiki_kanji_scrape.json') as data_file:    
    data = json.load(data_file)
    total_count = 0
    kanji_exist_count = 0
    for i in range(0,len(data)):
        total_count += 1
        
        gradenumber = int(data[i]["grade"])
        kanji_exists = Kanji.objects.filter(kanji_name = data[i]["kanji"]).exists()
        if kanji_exists:
            # the_kanji = Kanji.objects.get(kanji_name = data[i]["kanji"],readings = data[i]["kun_on_readings"], kanji_meaning = data[i]["meaning"], strokes = data[i]["strokes"], grade = gradenumber)
            the_kanji = Kanji.objects.get(kanji_name = data[i]["kanji"])
            the_kanji.readings = data[i]["kun_on_readings"]
            the_kanji.on_kun_readings = data[i]["romaji_readings"][1:]
            the_kanji.kanji_meaning = data[i]["meaning"]
            the_kanji.strokes = data[i]["strokes"]
            the_kanji.grade = gradenumber
            the_kanji.save()
            kanji_exist_count = kanji_exist_count + 1
        else:
            new_kanji = Kanji(kanji_name = data[i]["kanji"],readings = data[i]["kun_on_readings"], on_kun_readings = data[i]["romaji_readings"][1:],  kanji_meaning = data[i]["meaning"], strokes = data[i]["strokes"], grade = gradenumber)
            new_kanji.save()
            print data[i]["kanji"], "not in db  ", data[i]["kun_on_readings"], data[i]["romaji_readings"], data[i]["meaning"], data[i]["strokes"], gradenumber
            
    print kanji_exist_count,"  ", total_count        
        # Kanji(kanji_name = data[i]["kanji"],readings = data[i]["readings"], kanji_meaning = data[i]["meaning"], strokes = data[i]["strokes"], grade = gradenumber).save()
        
data_file.close()        
# print data


execfile('xmltodict/jlpt_upload_script.py')
execfile('xmltodict/all_word_upload.py')
execfile('xmltodict/frequency_parser.py')
execfile('xmltodict/kanji_word_matcher.py')
execfile('xmltodict/new_xml_parser.py')
        