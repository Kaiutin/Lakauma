# This file is part of Loukku, an application to display available rental apartments on Google Maps map.
# Copyright (C) 2013  Anton Laurila, Jari-Matti Kankaanpää, Samuel Uusi-Mäkelä
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# For more information, please refer to LICENCE file found in /Lakauma,
# or <http://www.gnu.org/licenses/> and GNU Affero General Public License

#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2


# City number
city = "259"

# Every entry in this dict corresponds to room number and a boolean
# to signify if the corresponding room number should be selected for current search
rooms = {"1":"1", "2":"1","3":"1","4":"1","5":"1"}
url = 'http://sato.fi/cps/sato/hs.xsl/-/html/hakutulos_vuokra.htm?cityname=&dd_city={0}&dd_district=&dd_rooms1={1}&dd_rooms2={2}&dd_rooms3={3}&dd_rooms4={4}&dd_rooms5={5}&dd_areafrom=0&dd_areato=99999&dd_page=1&dd_rentfrom=0&dd_rentto=99999&dd_results=10'.format(city,rooms["1"],rooms["2"],rooms["3"],rooms["4"],rooms["5"])
usock = urllib2.urlopen(url)
data = usock.read()
usock.close()


soppa = BeautifulSoup(data)
soppa.prettify()
soppa.td.a['href'](text)
