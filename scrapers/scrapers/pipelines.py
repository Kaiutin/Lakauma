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
            item['osoite'] = str(item['osoite'].replace("\\xe4", u'\xe4').encode('utf-8'))
            place, (lat, lng) = oma_geocode(item['osoite'] + "Jyväskylä")
            item["lat"] = lat
            item["lng"] = lng
        return item

def oma_geocode(address):
    time.sleep(0.5)
    geocoder = geocoders.GoogleV3()
    return geocoder.geocode(address)

