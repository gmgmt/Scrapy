# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WenkuxiazaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    summary=scrapy.Field()
    url=scrapy.Field()
    MD5_url=scrapy.Field()
    status=scrapy.Field()
    status_test=scrapy.Field()

