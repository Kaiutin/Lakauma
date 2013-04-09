# -*- coding: utf-8 -*-
# @author: Samuel Uusi-Makela
# @version: 8.4.2013
#
# Module to extract information from html code. Also includes
# method for returning substring of a string between 
# two substrings.
# Modify the keywords to find results from lines containing keywords.

#####  HUOM: Koodi on vielä hyvin vaiheessa, selitän jahka pääsen ilokiveltä

from ftfy import fix_text

# Extract data from html string s between two strings start and end.
def html_ext_between(s, start, end): 
    """ Extract string from between two defined strings start and end
        Usage:

        >string_smthing = "<a> hereissomethinguseful </a>"
        >print html_ext_between(string_smthing, "<a>", "</a>") 
       
        hereissomethinguseful
    """
    return "lol"
    

# Extract a substring from a string s which is between defined strings start and end.
def sub_str_extract(s, start, end):
    pass

class OVVItem():
    tyyppi ="" 
    neliot = "" 
    vuokra = ""
    osoite = ""
    vapautuu =""

# Insert the page specific keywords here
keywords = ["itemTitle","itemPrice","itemSize","itemFree","itemText"]
keyword_start = "resultItem"
keyword_end = "itemLink"
results = []
lippu = False
test_html = open('ovv_sorsa', 'r')
stripped_results = []
index = 0
w

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
    print stripped_results
    if(flag == True): 
        stripped_results.append(nearly[0])
        flag = False
        index = index + 1
    else:
        stripped_results[index].append()
        
