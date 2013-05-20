# -*- coding: utf-8 -*-
# This file is part of Loukku, an application to display available rental apartments on Google Maps map.
# Copyright (C) 2013  Anton Laurila, Jari-Matti Kankaanpää, Samuel Uusi-Mäkelä
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# For more information, please refer to LICENCE file found in /Lakauma,
# or <http://www.gnu.org/licenses/> and GNU Affero General Public License


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
