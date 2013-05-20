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
from bs4 import BeautifulSoup

url = "http://jyy.fi/opiskelijalle/asuminen-ja-toimeentulo/asunnot/vapaat-asunnot/"
response = urllib2.urlopen(url)
htmlparser = etree.HTMLParser()
tree = etree.parse(response, htmlparser)
huoneistot = []
soppa = BeautifulSoup(tree)
keitto = soppa.findAll('/div[@class="event-detail"]/text()')

for x in keitto:
    print x.strip()
    if (len(x) < 6):
        print ''.join(alkio for alkio in x if alkio.isdigit())
    else:
        print x



#tied = open('kortepohja_json.json', 'w')

#tied.write(json.dumps(huoneistot, sort_keys = False, indent = 4))


