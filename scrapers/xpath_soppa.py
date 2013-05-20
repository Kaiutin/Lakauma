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


import json
import urllib2
from lxml import etree
from geocode import oma_geocode

url = "http://www.kortepohja.fi/products/viewcategory/7/16/"
response = urllib2.urlopen(url)
htmlparser = etree.HTMLParser()
tree = etree.parse(response, htmlparser)
xs_vuokra = tree.xpath('//div[@class="block3"]/text()')
xs_osoite = tree.xpath('//h3/text()')
xs_neliot = tree.xpath('//div[@class="block1"]/text()')
xs_tyyppi = tree.xpath('//*[@id="fi"]/div/div/div/ul/li/div/a/text()')
xs_linkki = tree.xpath('//*[@id="fi"]/div/div/div/ul/li/div/a/@href')
xs = zip (xs_vuokra, xs_neliot,xs_tyyppi, xs_linkki)
huoneistot = []
for x in xs:
    huoneisto =  {"osoite": "","neliot":"","vuokra":"","tyyppi":"","lat":"","lng":"","linkki":"","tarjoaja":""}
    huoneisto["osoite"] = xs_osoite[0].split(",")[1].strip()
    huoneisto["tyyppi"] = x[2].strip()
    huoneisto["vuokra"] = ''.join(c for c in (x[0].strip()) if c.isdigit())
    huoneisto["neliot"] = x[1].strip()
    huoneisto["linkki"] = x[3]
    place, (lat, lng) = oma_geocode(huoneisto["osoite"] + u'Jyväskylä')
    huoneisto['lat'] = lat
    huoneisto['lng'] = lng
    huoneisto["tarjoaja"] = u'Kortepohja'
    huoneistot.append(huoneisto)
tied = open('kortepohja_json.json', 'w')

tied.write(json.dumps(huoneistot, sort_keys = False, indent = 4))
#'//*[@id="fi"]/div/div/div/ul/li


