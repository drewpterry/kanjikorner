#execfile('xmltodict/frequency_parser.py')
from manageset.models import UserProfile, Sets, Words, Kanji, WordMeanings

fyle = open("xmltodict/frequency_lists/base_aggregates.txt")

count = 0
count_1 = 0
count_more = 0
count_more_gte = 0
for lyne in fyle:
    entry = lyne.split()[1]
    entry_frequency = lyne.split()[0]
    the_word = Words.objects.filter(real_word = entry)
    frequency_exists = False
    #number of words
    number_of_words = len(the_word)
    if number_of_words >0:
        
        if number_of_words == 1:
            
            word_instance = Words.objects.get(real_word = entry)
            word_instance.frequency_two = entry_frequency
            word_instance.save()
           
            
        elif number_of_words > 1:
                
        
        
            for each in the_word:
                if each.frequency > 0:
                    frequency_exists = True
                    
                    
            if frequency_exists:
                for each in the_word:
                    
                    each.duplicate_word = True
                
                    if each.frequency > 0:
                        each.frequency_two = entry_frequency
                        each.published = True    
                        
                    each.save()
                print "frequency exists"    
                    
            else:
                print "didn't exist"
                for each in the_word:
                    each.frequency_two = entry_frequency
                    each.duplicate_word = True
                    each.published = False
                        
                    each.save()
                        
                        
                         
            
                  
              
        count += 1
        print entry_frequency, ' count:', count
fyle.close()

