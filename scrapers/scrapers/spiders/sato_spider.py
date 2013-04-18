# -*- coding: utf-8 -*-

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapers.items import VuokraKohdeItem
from ftfy import fix_text
#from geopy import geocoders


#Spider hakemaan asuntokohteiden tietoa sato.fi sivulta. 
#TODO: muokkaa hakemaan kaikki tiedot
class SatoSpider(BaseSpider):
   name = "sato" #This is the name you use to call the spider from update script.
   allowed_domains = ["sato.fi"]
   start_urls = ["http://sato.fi/cps/sato/hs.xsl/-/html/hakutulos_vuokra.htm?cityname=&dd_city=259&dd_district=&dd_rooms1=1&dd_rooms2=1&dd_rooms3=1&dd_rooms4=1&dd_rooms5=1&dd_areafrom=0&dd_areato=99999&dd_rentfrom=0&dd_rentto=99999&dd_results=10"]

   def parse(self, response):
       hxs = HtmlXPathSelector(response)
       sitesOsoite = hxs.select('//td[(((count(preceding-sibling::*) + 1) = 4) and parent::*)][normalize-space()]')
       sitesVuokra = hxs.select('//td[(((count(preceding-sibling::*) + 1) = 6) and parent::*)]')
       sitesNeliot = hxs.select('//td[(((count(preceding-sibling::*) + 1) = 5) and parent::*)]')
       sitesTyyppi = hxs.select('//td[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//a')
       sites = zip(sitesOsoite, sitesVuokra, sitesNeliot, sitesTyyppi)
       items = []
 #      geocoder = geocoders.MediaWiki("http://wiki.case.edu/%s")
       for site in sites:
           item = VuokraKohdeItem()
           parsimaton_osoite = str(site[0].select('text()[normalize-space()]').extract()).split("\'")
           item["osoite"] = parsimaton_osoite[1]
           vajaa = str(site[1].select('text()[normalize-space()]').extract()).split(" ")
           parempi = vajaa[0].split("\'") 
           item["vuokra"] = str(parempi[1])
           neliot_vaihe1 = str(site[2].select('text()[normalize-space()]').extract()).split(" ")
           neliot_vaihe2 = neliot_vaihe1[0].split("\'")
           item["neliot"] = str(neliot_vaihe2[1].replace(',','.'))
           vajaa_tyyppi =  str(site[3].select('text()[normalize-space()]').extract()).split("\'")           
           item["tyyppi"] = vajaa_tyyppi[1]
  #         place, (lat, lng) = geocoder.geocode(parsimaton_osoite[1])  
  #         item["lat"] = lat
  #         item["lng"] = lng
           items.append(item)
       return items

