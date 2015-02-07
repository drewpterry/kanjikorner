#execute this in django shell: execfile('xmltodict/new_xml_parser.py')
import xml.etree.ElementTree as ET
from manageset.models import UserProfile, Sets, Words, Kanji, WordMeanings
tree = ET.parse('xmltodict/frequency_lists/JMdict_e.xml')
root = tree.getroot()

# print root
#

i = 0
exist_count = 0
non_exist_count = 0
for child in root.iter('entry'):
    
    
    seq = child.find('ent_seq').text
    
    
    keb = child.findall('k_ele')
    rel = child.findall('r_ele')
    sense = child.find('sense')


    # print seq

    kanji_list = []
    frequency = []
    part_of_speech = []
    hirigana = []
    frequency2 = []
    for each in rel:
        hirigana.append(each.find('reb').text)
        if each.find('re_pri') != None:
            frequency2.append(each.find('re_pri').text)

    glosses = []
    for each in sense.iter():
        pos = each.findall('pos')
        gloss = each.findall('gloss')
        for each in pos:
            part_of_speech.append(each.text)

        for each in gloss:
            glosses.append(each.text)

    for each in keb:
        keb_word = each.find('keb').text

        the_word = Words.objects.filter(real_word = keb_word, hiragana = hirigana[0], meaning = glosses[0])


        # print keb_word
        if the_word.exists():
            the_word_instance = Words.objects.get(real_word = keb_word, hiragana = hirigana[0], meaning = glosses[0])
            # the_word_instance = Words.objects.get(real_word = keb_word)

            # print "exists: ", keb_word, the_word_instance
            for each in sense.iter():
                pos = each.findall('pos')
                gloss = each.findall('gloss')
                for each in pos:
                    part_of_speech.append(each.text)

                for each in gloss:
                    # glosses.append(each.text)
                    the_gloss = each.text
                    word_meaning_check = WordMeanings.objects.filter(word = the_word_instance, meaning = the_gloss).exists()
                    if word_meaning_check:
                        exist_count += 1
                        # print "meaning already exists"
                    else:
                        new_meaning = WordMeanings(word = the_word_instance, meaning = the_gloss)
                        new_meaning.save()
                        non_exist_count+=1
        else:
            # print "does not exist: ", keb_word
            pass
        
    i = i + 1
            
    print i, "exist: ", exist_count, "nope", non_exist_count
