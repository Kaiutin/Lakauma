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

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapers.items import VuokraKohdeItem


#Spider hakemaan Kortepohjan asuntokohteiden tietoa kortepohja.fi sivulta. 
class KortepohjaSpider(BaseSpider):
    name = "kortepohja" #This is the name you use to call the spider from update script.
    allowed_domains = ["kortepohja.fi"]
    start_urls = ["http://www.kortepohja.fi/products/viewcategory/2/16/"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        osoite_apu = hxs.select('//h3/text()').extract()[0].split(",")
        osoite = osoite_apu[1]
      
        sitesNeliot = hxs.select('//li[not(@class)]/div[@class="block1"]')
        #print(sitesNeliot)
        sitesVuokra = hxs.select('//li[not(@class)]/div[@class="block3"]')
        #print(sitesVuokra)
        sitesLinkki = hxs.select('//ul/li/div/a')
        #print(sitesLinkki)
        sitesTyyppi = hxs.select('//ul/li/div/a')

        sites = zip(sitesNeliot, sitesVuokra, sitesLinkki, sitesTyyppi)
        items = []
        for site in sites:
            item = VuokraKohdeItem()        
            item['osoite'] = osoite.strip()
            
            item["neliot"] = ''.join(alkio for alkio in(str(site[0].select('text()').extract()).strip()) if (alkio.isdigit() or alkio == ','))

            item["vuokra"] = ''.join(alkio for alkio in(str(site[1].select('text()').extract()).strip()) if alkio.isdigit())[:-2]
 
            item["linkki"] = str(site[2].select('@href').extract()).strip()

            item["tyyppi"] = ''.join(alkio for alkio in(str(site[3].select('text()').extract()).strip()) if alkio.isdigit())
            item['tarjoaja'] = "Kortepohja"
            items.append(item)
        return items
