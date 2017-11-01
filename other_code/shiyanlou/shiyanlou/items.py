# -*- coding: utf-8 -*-

import scrapy


class CourseItem(scrapy.Item):
    '''将每个要爬取得数据声明为 scrapy.Field()'''
    name = scrapy.Field()
    description = scrapy.Field()
    type = scrapy.Field()
    students = scrapy.Field()
