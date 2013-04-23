# Define here the models for your scraped items
# 
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class VuokraKohdeItem(Item):
    osoite = Field()
    neliot = Field()
    vuokra = Field()
    tyyppi = Field()
    lat = Field()
    lng = Field()
    linkki = Field()
    tarjoaja = Field()
