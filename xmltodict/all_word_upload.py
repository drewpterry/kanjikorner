#execute this in django shell: execfile('xmltodict/all_word_upload.py')
import json
from manageset.models import UserProfile, Sets, Words, Kanji
from pprint import pprint

with open('xmltodict/word_list.json') as data_file:    
    data = json.load(data_file)
    count = 0
    exist_count = 0
    new_word_count = 0
    for i in range(0,len(data)):
       
        
        word_check = Words.objects.filter(real_word = data[i]["full_word"],meaning = data[i]["definitions"][0], hiragana = data[i]["hiragana"], frequency = data[i]["frequency"])
        # print word_check
        if word_check.exists():
            
            exist_count += 1
        else:
            
            Words(real_word = data[i]["full_word"],meaning = data[i]["definitions"][0], hiragana = data[i]["hiragana"], frequency = data[i]["frequency"]).save()
            print "not exist"
            
            new_word_count = new_word_count + 1
        count = count + 1    
        print count, "new word count:", new_word_count, "exists:", exist_count
        
    
    
# print data