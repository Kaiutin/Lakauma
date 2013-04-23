# -*- coding: utf-8 -*-

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapers.items import VuokraKohdeItem


#Spider hakemaan Keltinmäen asuntokohteiden tietoa koas.fi sivulta. 
#TODO: muokkaa hakemaan kaikki tiedot
class KoasSpider(BaseSpider):
    name = "koas" #This is the name you use to call the spider from update script.
    allowed_domains = ["koas.fi"]
    start_urls = ["http://koas.fi/fi/kohteet/keltinmaki/", "http://koas.fi/fi/kohteet/jyvanen", "http://koas.fi/fi/kohteet/veturi"] # "http://koas.fi/fi/kohteet/roninmaki", "http://koas.fi/fi/kohteet/myllyjarvi", "http://koas.fi/fi/kohteet/ristonmaa", "http://koas.fi/fi/kohteet/hospa", "http://koas.fi/fi/kohteet/konsa", "http://koas.fi/fi/kohteet/letkut", "http://koas.fi/fi/kohteet/ratapiha", "http://koas.fi/fi/kohteet/kotiraide", "http://koas.fi/fi/kohteet/tahkonkaari", "http://koas.fi/fi/kohteet/koppari", "http://koas.fi/fi/kohteet/palstatie-3", "http://koas.fi/fi/kohteet/palstatie-4", "http://koas.fi/fi/kohteet/ykkospesa", "http://koas.fi/fi/kohteet/etela-kekkola", "http://koas.fi/fi/kohteet/ainola", "http://koas.fi/fi/kohteet/sillanpaa", "http://koas.fi/fi/kohteet/tango", "http://koas.fi/fi/kohteet/humppa", "http://koas.fi/fi/kohteet/ai", "http://koas.fi/fi/kohteet/rantapolku", "http://koas.fi/fi/kohteet/auvilankuja", "http://koas.fi/fi/kohteet/laajavuori", "http://koas.fi/fi/kohteet/taitoniekantie"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        osoite = hxs.select('//*[contains(concat( " ", @class, " " ), concat( " ", "campus-address", " " ))]//p')
        sitesNeliot = hxs.select('//*[contains(concat( " ", @class, " " ), concat( " ", "area", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "area", " " ))]')
        sitesVuokra = hxs.select('//*[contains(concat( " ", @class, " " ), concat( " ", "rent", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "rent", " " ))]')
        sitesTyyppi = hxs.select('//*[contains(concat( " ", @class, " " ), concat( " ", "apartment-type", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "rooms", " " ))]')
        sites = zip(sitesNeliot, sitesVuokra, sitesTyyppi)
        items = []

        for site in sites:
            item = VuokraKohdeItem()                  
            neliot_apu =  str(site[0].select('text()[normalize-space()]').extract()).split("\'")
            if neliot_apu[0] != '[]':
                item["neliot"] = neliot_apu[1]
            else:
                item["neliot"] = ''
            vuokra_apu = str(site[1].select('text()[normalize-space()]').extract()).split("\'")
            item["vuokra"] = vuokra_apu[1]
            tyyppi_apu = str(site[2].select('text()[normalize-space()]').extract()).split("\'")
            if tyyppi_apu[0] != '[]':
                item["tyyppi"] = tyyppi_apu[1]
            else:
                item["tyyppi"] = ''
            osoite_apu = str(osoite.select('text()[normalize-space()]').extract()).split("\'")       
            item["osoite"] = (osoite_apu[1]).replace("\\n\\t", "")
            print item["osoite"]
            item["linkki"] = response.url
            item["tarjoaja"] = "KOAS"
            
            #item["lat"] = 
            #item["lng"] =            
            items.append(item)
        return items
