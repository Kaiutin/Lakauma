# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider
from scrapy.selector import HtmlXPathSelector
from scrapers.items import VuokraKohdeItem
from ftfy import fix_text
from scrapy.shell import inspect_response 


#Spider hakemaan asuntokohteiden tietoa sato.fi sivulta. 
#TODO: muokkaa hakemaan kaikki tiedot
class SatoSpider(CrawlSpider):
   name = "sato2"
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
           items.append(item)
       request = Request("javascript:changePageTo2",
                   callback=self.parse_page2)
       return items + request
 

#
#   def parse(self, response):
#       hxs = HtmlXPathSelector(response)
#       sitesOsoite = hxs.select('//td[(((count(preceding-sibling::*) + 1) = 4) and parent::*)][normalize-space()]')
#       sitesVuokra = hxs.select('//td[(((count(preceding-sibling::*) + 1) = 6) and parent::*)]')
#       sitesNeliot = hxs.select('//td[(((count(preceding-sibling::*) + 1) = 5) and parent::*)]')
#       sitesTyyppi = hxs.select('//td[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//a')
#       sites = zip(sitesOsoite, sitesVuokra, sitesNeliot, sitesTyyppi)
#       items = []
#       for site in sites:
#           item = VuokraKohdeItem()
#           parsimaton_osoite = str(site[0].select('text()[normalize-space()]').extract()).split("\'")
#           item["osoite"] = parsimaton_osoite[1]
#           vajaa = str(site[1].select('text()[normalize-space()]').extract()).split(" ")
#           parempi = vajaa[0].split("\'") 
#           item["vuokra"] = str(parempi[1])
#           neliot_vaihe1 = str(site[2].select('text()[normalize-space()]').extract()).split(" ")
#           neliot_vaihe2 = neliot_vaihe1[0].split("\'")
#           item["neliot"] = str(neliot_vaihe2[1].replace(',','.'))
#           vajaa_tyyppi =  str(site[3].select('text()[normalize-space()]').extract()).split("\'")           
#           item["tyyppi"] = vajaa_tyyppi[1]
#           items.append(item)
#       return items
###

class SatoSpider(CrawlSpider):
        name = "sato3"
        allowed_domains = [ "sato.fi" ]
           start_urls = ["http://sato.fi/cps/sato/hs.xsl/-/html/hakutulos_vuokra.htm?cityname=&dd_city=259&dd_district=&dd_rooms1=1&dd_rooms2=1&dd_rooms3=1&dd_rooms4=1&dd_rooms5=1&dd_areafrom=0&dd_areato=99999&dd_rentfrom=0&dd_rentto=99999&dd_results=10"]

        rules = (
                Rule(SgmlLinkExtractor(allow=('sato\.fi', 'page='), restrict_xpaths = '//div*/span[@class="borderless"]'), callback='parse2'),
        )

        def parse2(self, response):
                hxs = HtmlXPathSelector(response)
                items = []
                countries = hxs.select('//div[@class="index-content"]')
                tmpNextPage = hxs.select('//div[@class="paginator"]/span[@id="next"]/a/@href').extract()
                for country in countries:
                        item = FoodItem()
                        countryName = country.select('.//h3/text()').extract()
                        item['country'] = countryName
                        print "Country Name: ", countryName
                        shows = country.select('.//div[@class="content1"]')
                        for show in shows.select('.//div'):
                                showLink = (show.select('.//h4/a/@href').extract()).pop()
                                showLocation = show.select('.//h4/a/text()').extract()
                                showText = show.select('.//p/text()').extract()
                                item['showURL'] = "http://www.travelchannel.com"+str(showLink)
                                item['showcity'] = showLocation
                                item['showtext'] = showText
                                item['showtext'] = showText
                                print "\t", showLink
                                print "\t", showLocation
                                print "\t", showText
                                print "\n"
                                items.append(item)
                        **#return items**

                for NextPageLink in tmpNextPage:
                        m = re.search("Location", NextPageLink)
                        if m:
                                NextPage = NextPageLink
                                print "Next Page:  ", NextPage
                                yield Request("http://www.example.com/"+NextPage, callback = self.parse)
                        else:
                                NextPage = 'None'
SPIDER = food()

def write_file(taulu):
    f = open('items', 'w')
                

