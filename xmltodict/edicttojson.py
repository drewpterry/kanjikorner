import xmltodict, json

# file_object = open('JMdict_e_sample.xml','r')
file_object = open('JMdict_e.xml','r')
o = xmltodict.parse(file_object)
thejson = json.dumps(o)
thejson = json.loads(thejson)




print "writing the file-----------------------"




def word_filter(element, element2, thejson):
    try:
        thejson[element][0][element2]
    except Exception:
        try:
            thejson[element][element2]
        except Exception:    
            multiple_readings = None
        else:    
            multiple_readings =  False
        pass
    else:
        multiple_readings = True

    if multiple_readings == False:
        hiragana = thejson[element][element2]
    elif multiple_readings == True :
        hiragana = thejson[element][0][element2]
    else:
        hiragana = "none"
    
    # if element == "r_ele":
#         #print "the hiragana is " + hiragana +  "."
#     else:
#         print "the actual word is " + hiragana + "."
    return hiragana    




#definition
def def_finder(thejson):
    try:
        thejson['sense']['gloss'][0]["#text"]
    except Exception:
        try:
            thejson['sense']['gloss']["#text"]
        except Exception:
            multiple_readings = None
        else:
            multiple_readings =  False
    else:
        multiple_readings = True
    
    if multiple_readings == False:
        definition = thejson['sense']['gloss']["#text"]
    elif multiple_readings == True :
        definition = thejson['sense']['gloss'][0]["#text"]
    else:
        try:
            thejson['sense'][0]['gloss'][0]["#text"]
        except Exception:
            try:
                thejson['sense'][0]['gloss']["#text"]
            except Exception:
                definition = "none"
            else:
                definition = thejson['sense'][0]['gloss']["#text"]     
        else:
            definition = thejson['sense'][0]['gloss'][0]["#text"]     
    # print thejson['sense']['gloss']["#text"]
    #print "the definition is " + definition
    return definition

        

count = 0
# print thejson['sense']['gloss'][0]["#text"]
# #print thejson["k_ele"]
def frequency(thejson):
    try:
        thejson["k_ele"][0]["ke_pri"]
    except Exception:
        try:
            thejson["k_ele"]["ke_pri"]    
        except Exception:
            frequency = 0
        else:
            frequency = thejson["k_ele"]["ke_pri"]
    else:
        frequency = thejson["k_ele"][0]["ke_pri"]
        
    global count
    place = ''
    number = 0
    if "nf" in str(frequency):
        count = count + 1
        place = str(frequency).find("nf")
        number = str(frequency)[place+2:place+4]
        number = int(number)
    # print frequency, "the count is:" + str(count), number
    return number    


thejson = thejson["JMdict"]["entry"]
def all_results(thejson):
    clean_json = []
    for entry in thejson:
        #print entry
    #hiragana
        hiragana = word_filter("r_ele", "reb", entry)
        #actual word
        full_word = word_filter("k_ele","keb", entry)
        definition = def_finder(entry)
        frequency_all = frequency(entry)

        clean_json.append({"full_word": full_word, "hiragana": hiragana , "definitions": [definition], "frequency" : frequency_all})
        # print "-------------------"
#         print entry
#     print clean_json   
    return clean_json
        # print clean_json
        
the_full_list =  all_results(thejson)
    
        


with open('word_list.json', 'w') as outfile:
  json.dump(the_full_list, outfile, indent = 1)
  
 
print "file: 'word_list.json' written!" 

#[{"full_word": asdf, "hiragana": adsf, "definitions": [{"definition":asdfsadf}, {"defition" : alsdfsad}], "frequency" : asd]