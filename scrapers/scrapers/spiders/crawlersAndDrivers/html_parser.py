# -*- coding: utf-8 -*-       +358400444588
# @author: Samuel Uusi-Makela
# @version: 8.4.2013
#
# Module to extract information from html code. Also includes
# method for returning substring of a string between 
# two substrings.
# Modify the keywords to find results from lines containing keywords.


from ftfy import fix_text
from bs4 import BeautifulSoup

def parseilu():
    # Insert the page specific keywords here
    keywords = ["itemTitle","itemPrice","itemSize","itemFree","itemText"]
    keyword_start = "resultItem"
    keyword_end = "itemLink"
    results = []
    lippu = False
    test_html = open('ovv_sorsa', 'r')
    stripped_results = []
    flag = True

    for line in test_html:
        if (keyword_end in line and lippu == True):
            lippu = False
        if (keyword_start in line and lippu == False):
            lippu = True    
        if (lippu == True):    
            for word in keywords:
                if (word in line):
                    results.append(line)
    for result in results:
        fixed1 = result.decode('utf-8')
        fixed2 = fix_text(fixed1)
        almost = fixed2.strip()
        better = almost.split('>')
        even_better = better[1]
        nearly = even_better.split('<')
        if(flag == True): 
            stripped_results.append([nearly[0]])
            flag = False
        else:
            stripped_results[len(stripped_results)-1].append(nearly[0])
            ###  !!!!!! TODO: TEE PALJON PAREMMAKSI 
            if('Jyv' in nearly[0]):
                flag = True
    for kohde in stripped_results:
        apartment = VuokraKohdeItem()
        apartment.osoite
        apartment.vuokra
        apartment.neliot
        apartment.tyyppi
        apartment.lat
        apartment.lng
        apartment.linkki
    return HttpResponse(json.dumps(lista))

class 
