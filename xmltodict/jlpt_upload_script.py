# -*- coding: utf-8 -*-
#execfile('xmltodict/jlpt_upload_script.py')
from manageset.models import UserProfile, Sets, Words, Kanji, WordMeanings

newspaper_kanji = open("xmltodict/frequency_lists/newspaper_kanji/complete_kanji_frequency_newspaper.csv")
fyle = open("xmltodict/frequency_lists/jlptkanji/tangorin_20001.csv")
file_n2 = open("xmltodict/frequency_lists/jlptkanji/tangorin_20002.csv")
file_n3 = open("xmltodict/frequency_lists/jlptkanji/tangorin_20003.csv")
file_n4 = open("xmltodict/frequency_lists/jlptkanji/tangorin_20004.csv")
file_n5 = open("xmltodict/frequency_lists/jlptkanji/tangorin_20005.csv")
jinmei = open("xmltodict/frequency_lists/jinmeiyo/tangorin_1000.csv")

count = 0
in_db = 0
news_paper_frequency = 0
# for lyne in newspaper_kanji:
#     # print lyne
#
#
#     entry = lyne.split('\t')
#     kanji_symbol = entry[0]
#     readings = entry[1].replace(' ・ ', ", ")
#     definition = entry[2]
#     first_def = definition.split(';')[0]
#
#     the_kanji_exists = Kanji.objects.filter(kanji_name = kanji_symbol).exists()
#     news_paper_frequency += 1
#     count += 1
#     print kanji_symbol, news_paper_frequency, readings
#     if the_kanji_exists:
#         the_kanji_object = Kanji.objects.get(kanji_name = kanji_symbol)
#         the_kanji_object.newspaper_frequency = news_paper_frequency
#         the_kanji_object.save()
#
#         in_db += 1
#     else:
#         new_kanji = Kanji(kanji_name = kanji_symbol, kanji_meaning = first_def, on_kun_readings = readings, newspaper_frequency = news_paper_frequency)
#         new_kanji.save()
#         # print kanji_symbol, readings, first_def[0]
#
#
#     # news_paper_frequency += 1
#   #   count += 1
#     # print ' count:', count, in_db
#     # print kanji_symbol, news_paper_frequency
# newspaper_kanji.close()
#
#
#
# for lyne in file_n5:
#      entry = lyne.split('\t')
#      kanji_symbol = entry[0]
#      readings = entry[1].replace(' ・ ', ", ")
#      definition = entry[2]
#      first_def = definition.split(';')[0]
#
#      the_kanji_exists = Kanji.objects.filter(kanji_name = kanji_symbol).exists()
#
#      count += 1
#      print kanji_symbol, news_paper_frequency, readings
#      if the_kanji_exists:
#          the_kanji_object = Kanji.objects.get(kanji_name = kanji_symbol)
#          the_kanji_object.jlpt_level = 5
#          the_kanji_object.save()
#
#          in_db += 1
#      else:
#          new_kanji = Kanji(kanji_name = kanji_symbol, kanji_meaning = first_def, on_kun_readings = readings, jlpt_level = 5)
#          new_kanji.save()
#          # print kanji_symbol, readings, first_def[0]
#
#
#      # news_paper_frequency += 1
#    #   count += 1
#      # print ' count:', count, in_db
#      # print kanji_symbol, news_paper_frequency
#
# file_n5.close()
#
#
#
#
# for lyne in file_n4:
#       entry = lyne.split('\t')
#       kanji_symbol = entry[0]
#       readings = entry[1].replace(' ・ ', ", ")
#       definition = entry[2]
#       first_def = definition.split(';')[0]
#
#       the_kanji_exists = Kanji.objects.filter(kanji_name = kanji_symbol).exists()
#
#       count += 1
#       print kanji_symbol, news_paper_frequency, readings
#       if the_kanji_exists:
#           the_kanji_object = Kanji.objects.get(kanji_name = kanji_symbol)
#           the_kanji_object.jlpt_level = 4
#           the_kanji_object.save()
#
#           in_db += 1
#       else:
#           new_kanji = Kanji(kanji_name = kanji_symbol, kanji_meaning = first_def, on_kun_readings = readings, jlpt_level = 4)
#           new_kanji.save()
#           # print kanji_symbol, readings, first_def[0]
#
#
#       # news_paper_frequency += 1
#     #   count += 1
#       # print ' count:', count, in_db
#       # print kanji_symbol, news_paper_frequency
# file_n4.close()
#
#
# for lyne in file_n3:
#       entry = lyne.split('\t')
#       kanji_symbol = entry[0]
#       readings = entry[1].replace(' ・ ', ", ")
#       definition = entry[2]
#       first_def = definition.split(';')[0]
#
#       the_kanji_exists = Kanji.objects.filter(kanji_name = kanji_symbol).exists()
#
#       count += 1
#       print kanji_symbol, news_paper_frequency, readings
#       if the_kanji_exists:
#           the_kanji_object = Kanji.objects.get(kanji_name = kanji_symbol)
#           the_kanji_object.jlpt_level = 3
#           the_kanji_object.save()
#
#           in_db += 1
#       else:
#           new_kanji = Kanji(kanji_name = kanji_symbol, kanji_meaning = first_def, on_kun_readings = readings, jlpt_level = 3)
#           new_kanji.save()
#           # print kanji_symbol, readings, first_def[0]
#
#
#       # news_paper_frequency += 1
#     #   count += 1
#       # print ' count:', count, in_db
#       # print kanji_symbol, news_paper_frequency
# file_n3.close()
#
#
#
#
#
# for lyne in file_n2:
#       entry = lyne.split('\t')
#       kanji_symbol = entry[0]
#       readings = entry[1].replace(' ・ ', ", ")
#       definition = entry[2]
#       first_def = definition.split(';')[0]
#
#       the_kanji_exists = Kanji.objects.filter(kanji_name = kanji_symbol).exists()
#
#       count += 1
#       print kanji_symbol, news_paper_frequency, readings
#       if the_kanji_exists:
#           the_kanji_object = Kanji.objects.get(kanji_name = kanji_symbol)
#           the_kanji_object.jlpt_level = 2
#           the_kanji_object.save()
#
#           in_db += 1
#       else:
#           new_kanji = Kanji(kanji_name = kanji_symbol, kanji_meaning = first_def, on_kun_readings = readings, jlpt_level = 2)
#           new_kanji.save()
#           # print kanji_symbol, readings, first_def[0]
#
# file_n2.close()
#
#
#
#
#
#
# for lyne in fyle:
#       entry = lyne.split('\t')
#       kanji_symbol = entry[0]
#       readings = entry[1].replace(' ・ ', ", ")
#       definition = entry[2]
#       first_def = definition.split(';')[0]
#
#       the_kanji_exists = Kanji.objects.filter(kanji_name = kanji_symbol).exists()
#
#       count += 1
#       print kanji_symbol, news_paper_frequency, readings
#       if the_kanji_exists:
#           the_kanji_object = Kanji.objects.get(kanji_name = kanji_symbol)
#           the_kanji_object.jlpt_level = 1
#           the_kanji_object.save()
#
#           in_db += 1
#       else:
#           new_kanji = Kanji(kanji_name = kanji_symbol, kanji_meaning = first_def, on_kun_readings = readings, jlpt_level = 1)
#           new_kanji.save()
#           # print kanji_symbol, readings, first_def[0]
#
#
#
# fyle.close()






for lyne in jinmei:
      print "what"
      entry = lyne.split('\t')
      kanji_symbol = entry[0]
      readings = entry[1].replace(' ・ ', ", ")
      definition = entry[2]
      first_def = definition.split(';')[0]
    
      the_kanji_exists = Kanji.objects.filter(kanji_name = kanji_symbol).exists()
     
      count += 1
      print kanji_symbol, news_paper_frequency, readings
      if the_kanji_exists:
          the_kanji_object = Kanji.objects.get(kanji_name = kanji_symbol)
          the_kanji_object.jinmeiyo = True
          the_kanji_object.save()
        
          in_db += 1
      else:
          new_kanji = Kanji(kanji_name = kanji_symbol, kanji_meaning = first_def, on_kun_readings = readings, jinmeiyo = True)
          new_kanji.save()
          # print kanji_symbol, readings, first_def[0]
        

     
fyle.close()








print ' count:', count, in_db
