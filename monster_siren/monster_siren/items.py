# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MonsterSirenItem(scrapy.Item):
    # define the fields for your item here like:
    is_album = scrapy.Field()
    name = scrapy.Field()
    album_id = scrapy.Field()
    source = scrapy.Field()
    suffix = scrapy.Field()
    pass
