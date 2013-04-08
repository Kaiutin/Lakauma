# @author: Samuel Uusi-Makela
# @version: 8.4.2013
#
# Module to extract information from html code. Also includes
# method for returning substring of a string between 
# two substrings.
# Modify the keywords to find results from lines containing keywords.

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

# Insert the page specific keywords here
keywords = ["itemTitle","itemPrice","itemSize","itemFree","itemText"]

results = []

test_html = open('ovv_sorsa', 'r')

i = 0

for line in test_html:
    for word in keywords:
       if word in line: 
            results.append(str(i))
            i = i + 1
print results
    
