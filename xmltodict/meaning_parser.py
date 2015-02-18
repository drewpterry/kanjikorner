#execute this in django shell: execfile('xmltodict/meaning_parser.py')
import xml.etree.ElementTree as ET
from manageset.models import UserProfile, Sets, Words, Kanji, WordMeanings
# tree = ET.parse('xmltodict/frequency_lists/JMdict_e.xml')
# root = tree.getroot()

# print root
#

i = 0
exist_count = 0
non_exist_count = 0

# get an iterable
context = ET.iterparse('xmltodict/frequency_lists/JMdict_e.xml', events=("start", "end"))

# turn it into an iterator
context = iter(context)

# get the root element
event, root = context.next()

# for event, elem in context:
#     if event == "end" and elem.tag == "record":
#         ... process record elements ...
#         root.clear()
for event, child in context:
    
    if child.tag == 'entry' and event == "start":
        for each in child:
            print each
        i += 1
        
        kanji_list = []
        frequency = []
        part_of_speech = []
        hirigana = []
        frequency2 = []
        
        sense = child.findall('sense')
        # keb = child.findall('k_ele')
        # rel = child.findall('r_ele')
        info = child.findall('info')
        
        
        
        # for each in rel:
 #            try:
 #                # print each.find('reb').text
 #                hirigana.append(each.find('reb').text)
 #                if each.find('re_pri') != None:
 #                    frequency2.append(each.find('re_pri').text)
 #            except:
 #                print "-----------------------------------------------------------------------------------------------"
        
        glosses = []
        # for each in sense:
#             try:
#                 pos = each.findall('pos')
#                 gloss = each.findall('gloss')
#                 for each in pos:
#                     part_of_speech.append(each.text)
#
#                 for each in gloss:
#                     # print each
#                     glosses.append(each.text)
#
#
#             except:
#                 print "---------------------"
                
                
        # for each in keb:
 #             keb_word = each.find('keb').text
 #             # print hirigana,"-------------------------", glosses
 #             the_word = Words.objects.filter(real_word = keb_word, hiragana = hirigana[0], meaning = glosses[0])
 #
 #
 #             # print keb_word
 #             if the_word.exists():
 #                 the_word_instance = Words.objects.get(real_word = keb_word, hiragana = hirigana[0], meaning = glosses[0])
 #                 # the_word_instance = Words.objects.get(real_word = keb_word)
 #
 #                 # print "exists: ", keb_word, the_word_instance
 #                 for each in sense:
 #                     pos = each.findall('pos')
 #                     gloss = each.findall('gloss')
 #                     for each in pos:
 #                         part_of_speech.append(each.text)
 #
 #                     for each in gloss:
 #                         # glosses.append(each.text)
 #                         the_gloss = each.text
 #                         word_meaning_check = WordMeanings.objects.filter(word = the_word_instance, meaning = the_gloss).exists()
 #                         if word_meaning_check:
 #                             exist_count += 1
 #                             # print "meaning already exists"
 #                         else:
 #                             new_meaning = WordMeanings(word = the_word_instance, meaning = the_gloss)
 #                             # new_meaning.save()
 #                             non_exist_count+=1
 #             else:
 #                 # print "does not exist: ", keb_word
 #                 pass

            # if glosses[0] == []:
#                 glosses[0] = "_________________________________________________________________________"
        # print i, child, event, hirigana, frequency2, glosses, part_of_speech
        if i == 34:
            break
        print i, glosses, sense
        # seq = child.find('ent_seq').text
 #
 #
 #        keb = child.findall('k_ele')
 #        rel = child.findall('r_ele')
 #        sense = child.find('sense')
 #
 #
 #        # print seq
 #
 #        kanji_list = []
 #        frequency = []
 #        part_of_speech = []
 #        hirigana = []
 #        frequency2 = []
 #        for each in rel:
 #            hirigana.append(each.find('reb').text)
 #            if each.find('re_pri') != None:
 #                frequency2.append(each.find('re_pri').text)
 #
 #        glosses = []
 #        for each in sense.iter():
 #            pos = each.findall('pos')
 #            gloss = each.findall('gloss')
 #            for each in pos:
 #                part_of_speech.append(each.text)
 #
 #            for each in gloss:
 #                glosses.append(each.text)
 #
 #        for each in keb:
 #            keb_word = each.find('keb').text
 #
 #            the_word = Words.objects.filter(real_word = keb_word, hiragana = hirigana[0], meaning = glosses[0])
 #
 #
 #            # print keb_word
 #            if the_word.exists():
 #                the_word_instance = Words.objects.get(real_word = keb_word, hiragana = hirigana[0], meaning = glosses[0])
 #                # the_word_instance = Words.objects.get(real_word = keb_word)
 #
 #                # print "exists: ", keb_word, the_word_instance
 #                for each in sense.iter():
 #                    pos = each.findall('pos')
 #                    gloss = each.findall('gloss')
 #                    for each in pos:
 #                        part_of_speech.append(each.text)
 #
 #                    for each in gloss:
 #                        # glosses.append(each.text)
 #                        the_gloss = each.text
 #                        word_meaning_check = WordMeanings.objects.filter(word = the_word_instance, meaning = the_gloss).exists()
 #                        if word_meaning_check:
 #                            exist_count += 1
 #                            # print "meaning already exists"
 #                        else:
 #                            new_meaning = WordMeanings(word = the_word_instance, meaning = the_gloss)
 #                            new_meaning.save()
 #                            non_exist_count+=1
 #            else:
 #                # print "does not exist: ", keb_word
 #                pass
 #
 #        i = i + 1
 #
 #        print i, "exist: ", exist_count, "nope", non_exist_count
        
    child.clear()    
    
    
    
