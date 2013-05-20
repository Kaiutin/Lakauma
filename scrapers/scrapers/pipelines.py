# This file is part of Loukku, an application to display available rental apartments on Google Maps map.
# Copyright (C) 2013  Anton Laurila, Jari-Matti Kankaanpää, Samuel Uusi-Mäkelä
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# For more information, please refer to LICENCE file found in /Lakauma,
# or <http://www.gnu.org/licenses/> and GNU Affero General Public License


# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

import json
import re
import codecs
from ftfy import fix_text
from items import VuokraKohdeItem
from geopy import geocoders
import time

class ScrapersPipeline(object):
    def process_item(self, item, spider):
        if(isinstance(item, VuokraKohdeItem)):
			item['osoite'] = str(item['osoite']).replace("\\xe4", u'\xe4').encode('utf-8')
            #place, (lat, lng) = oma_geocode(item['osoite'] + "Jyväskylä")
            #item["lat"] = lat
            #item["lng"] = lng
        return item

def oma_geocode(address):
    time.sleep(0.5)
    geocoder = geocoders.GoogleV3()
    return geocoder.geocode(address)

