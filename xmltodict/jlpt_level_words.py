#execute this in django shell: execfile('xmltodict/jlpt_level_words.py')
import json
from manageset.models import UserProfile, Sets, Words, Kanji
from pprint import pprint
import requests
from bs4 import BeautifulSoup
import csv
import sys



def scrape(word_object):
    # count = 0
    words_to_without_levels = Words.objects.filter(jlpt_level__isnull = True)
    headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.16 Safari/534.24"}
    # for each in words_to_without_levels:
    # print each.real_word
    # not working, not checking none
    if word_object.real_word == "none":
        target_url = "http://jisho.org/search/" + word_object.hiragana + "%23words"
    else:
        target_url = "http://jisho.org/search/" + word_object.real_word + "%23words"
    try:
        r = requests.get(target_url,headers=headers,timeout=45)   
    except:
        jlpt_level = u"error"
        # print (target_url, ' ',  rc)
        return [target_url, word_object.real_word, word_object.meaning, jlpt_level]
    # print target_url
    # count += 1
    # print count
    
    raw_html = r.text
    soup = BeautifulSoup(raw_html,"html.parser")
    try:
        jlpt_level = soup.find("span", class_="concept_light-tag label").contents
        jlpt_level = jlpt_level[0][-1]
    except:
        jlpt_level = "n/a"      
    return [target_url, word_object.real_word, word_object.meaning, jlpt_level]


def write_csv(output_file):
    count = 0
    with open(output_file,'wt') as fp:
        wr = csv.writer(fp, delimiter=";")
        wr.writerow(['count', 'url', 'word', 'meaning', 'jlpt level'])  
        words_to_without_levels = Words.objects.filter(jlpt_level__isnull = True)
        # for each in words_to_without_levels:
 #            count += 1
 #            scraped_info = scrape(each)
 #            wr.writerow([count,scraped_info[0].encode('utf-8'),scraped_info[1].encode('utf-8'),scraped_info[2].encode('utf-8'),scraped_info[3]])
 #            fp.flush()
 #            print count, scraped_info
        
        error_words = Words.objects.filter(jlpt_level = 6)
         
        for each in error_words:
            count += 1
            scraped_info = scrape(each)
            wr.writerow([count,scraped_info[0].encode('utf-8'),scraped_info[1].encode('utf-8'),scraped_info[2].encode('utf-8'),scraped_info[3]])
            fp.flush()
            print count, scraped_info   
write_csv("jlpt_word_test2.csv")    

# with open('xmltodict/word_list.json') as data_file:
#     data = json.load(data_file)
#     count = 0
#     exist_count = 0
#     new_word_count = 0
#     for i in range(0,len(data)):
#
#
#         word_check = Words.objects.filter(real_word = data[i]["full_word"],meaning = data[i]["definitions"][0], hiragana = data[i]["hiragana"], frequency = data[i]["frequency"])
#         # print word_check
#         if word_check.exists():
#
#             exist_count += 1
#         else:
#
#             Words(real_word = data[i]["full_word"],meaning = data[i]["definitions"][0], hiragana = data[i]["hiragana"], frequency = data[i]["frequency"]).save()
#             print "not exist"
#
#             new_word_count = new_word_count + 1
#         count = count + 1
#         print count, "new word count:", new_word_count, "exists:", exist_count
        
    
    
# print data