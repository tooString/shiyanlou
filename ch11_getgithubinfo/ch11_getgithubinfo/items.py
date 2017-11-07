# -*- coding: utf-8 -*-

import scrapy


class GetgithubinfoItem(scrapy.Item):
    name = scrapy.Field()
    update_time = scrapy.Field()
