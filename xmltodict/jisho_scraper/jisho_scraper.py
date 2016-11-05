from bs4 import BeautifulSoup
import requests
import csv
import sys
import json
from manageset.models import Words
from pprint import pprint


def scrape(word_object):
    # count = 0
    # words_to_without_levels = Words.objects.filter(jlpt_level__isnull = True)
    headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.16 Safari/534.24"}
    # for each in words_to_without_levels:
    # print each.real_word
    # not working, not checking none
    words = words = Words.objects.exclude(frequency_thousand = None).exclude(frequency_thousand__gte = 40).distinct()
    if word_object.real_word == "none":
        target_url = "https://tatoeba.org/eng/sentences/search?query=\"" + word_object.hiragana+ "\"&" + \
                      "from=jpn&to=eng&orphans=no&unapproved=no&native=yes&user=&tags=&has_audio=&" + \
                      "trans_filter=limit&trans_to=eng&trans_link=&trans_user=&trans_orphan=no&" + \
                      "trans_unapproved=no&trans_has_audio=&sort=created"
    else:
        # target_url = "http://jisho.org/search/" + word_object.real_word + "%23words"
        target_url = "https://tatoeba.org/eng/sentences/search?query=\"" + word_object.real_word + "\"&" + \
                      "from=jpn&to=eng&orphans=no&unapproved=no&native=yes&user=&tags=&has_audio=&" + \
                      "trans_filter=limit&trans_to=eng&trans_link=&trans_user=&trans_orphan=no&" + \
                      "trans_unapproved=no&trans_has_audio=&sort=created"
    try:
        r = requests.get(target_url,headers=headers,timeout=45)   
    except:
        jlpt_level = u"error"
        # print (target_url, ' ',  rc)
        return [target_url, word_object.real_word, word_object.meaning]
    # print target_url
    # count += 1
    # print count
    
    raw_html = r.text
    soup = BeautifulSoup(raw_html,"html.parser")
    try:
        list_of_sentences = soup.find_all(".sentences_set","text")
        for each in list_of_sentences:
            # if each.contents. == word_object.real_word:
            list_of_sentences
            tree_object = each.contents
            print tree_object[0].strip()
            print word_object.real_word
            # if tree_object[0] == word_object.real_word:
            print each.contents
            print "not working"
            sentence = ""    
    except:
        jlpt_level = "n/a"      
    return [target_url, word_object.real_word,, sentence, jlpt_level]


def write_csv(output_file):
    count = 0
    with open(output_file,'wt') as fp:
        wr = csv.writer(fp, delimiter=";")
        wr.writerow(['id', 'word', 'sentence', 'owner'])
        words = Words.objects.exclude(frequency_thousand = None).exclude(frequency_thousand__gte = 40).distinct()
        for each in words:
            count += 1
            scraped_info = scrape(each)
            wr.writerow([count,scraped_info[0].encode('utf-8'),scraped_info[1].encode('utf-8'),scraped_info[2].encode('utf-8'),scraped_info[3]])
            fp.flush()
            # print count, scraped_info

        # error_words = Words.objects.filter(jlpt_level = 6)

        for each in error_words:
            count += 1
            scraped_info = scrape(each)
            wr.writerow([count,scraped_info[0].encode('utf-8'),scraped_info[1].encode('utf-8'),scraped_info[2].encode('utf-8'),scraped_info[3]])
            fp.flush()
            # print count, scraped_info
write_csv("scrape_sentences.csv") 


# def sentence_scrape(output_file):
#     with open(output_file,'wt') as fp:
#         wr = csv.writer(fp, delimiter=";")
#         wr.writerow(['id', 'count' ,'word', 'sentence', 'jlpt level'])
#         words = words = Words.objects.exclude(frequency_thousand = None).exclude(frequency_thousand__gte = 40).distinct()
#         words_list = list(words)
#
#         i = 0
#         for each in words:
#
#             kanji = each.kanji.all()
#             id_list = set()
#             for kanji_id in kanji:
#                 id_list.add(kanji_id.id)
#
#
#             the_one_list = list(id_list - set(kanji_in))
#             print the_one_list
#
#             if the_one_list:
#                 print "hell0"
#                 words_list.remove(each)
#
#         for each in words_list:
#             print each,"got here"
#             wr.writerow([each.id, each.real_word.encode('utf-8'), each.jlpt_level])
#             fp.flush()
#
#
#     print words.count(), "finished"
    
    
    
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