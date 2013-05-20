#-*- coding: utf-8 -*-

# This file is part of Loukku, an application to display available rental apartments on Google Maps map.
# Copyright (C) 2013  Anton Laurila, Jari-Matti Kankaanpää, Samuel Uusi-Mäkelä
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# For more information, please refer to LICENCE file found in /Lakauma,
# or <http://www.gnu.org/licenses/> and GNU Affero General Public License

from bs4 import BeautifulSoup
import urllib2
from scrapy.item import Item, Field
from django.utils.encoding import smart_text
import json
from geocode import oma_geocode

def parse_ovv(data):
    soppa = BeautifulSoup(data)
    soppa.prettify()
    items = []
    kohteet = soppa.findAll('div', attrs={'class':'resultItem'})
    while(len(kohteet) > 0):
        kohde = kohteet.pop(0)
        huoneisto =  {"osoite": "","neliot":"","vuokra":"","tyyppi":"","lat":"","lng":"","linkki":"","tarjoaja":""}
        huoneisto["osoite"] = smart_text(kohde.find('div', attrs={'class':'itemText'}).string)
        huoneisto["tyyppi"] = smart_text(kohde.find('div', attrs={'class':'itemTitle'}).string)
        huoneisto["vuokra"] = ''.join(c for c in (smart_text(kohde.find('div', attrs={'class':'itemPrice'}).string)) if c.isdigit())
        huoneisto["neliot"] = smart_text(kohde.find('div', attrs={'class':'itemSize'}).contents[0].split()[0])
        print huoneisto["osoite"].split(",")[0] + " Jyvaskyla"
        try:
            place, (lat, lng) = oma_geocode(huoneisto["osoite"].split(",")[0] + " Jyvaskyla")
        except ValueError:
            place, (lat, lng) = oma_geocode(huoneisto["osoite"].split(",")[0] + " Jyvaskyla" + ", 40700")
        huoneisto['lat'] = lat
        huoneisto['lng'] = lng
        huoneisto['linkki'] = u'http://www.ovv.fi/asunto?' + 'asunto=' + (''.join(alkio for alkio in (smart_text(kohde.find('a')['onclick'])) if alkio.isdigit()))
        huoneisto["tarjoaja"] = u'OVV' 
        items.append(huoneisto)
        print len(kohteet)
    return json.dumps(items, sort_keys = False, indent = 4)
        
#
#<div class="itemTitle">1h+kk+kh</div>
#<div class="itemPrice">370€/kk</div>
#<div class="itemSize">20 m<sup>2</sup></div>
#<div class="itemFree">Vapaa: Heti</div>
#<div class="itemText">Piilukko 3, KORTEMÄKI, 40630 Jyväskylä</div>
#<div class="itemLinks"><a onclick="asunto(65619)">Lisätiedot, hakuvahti &gt;</a></div>
