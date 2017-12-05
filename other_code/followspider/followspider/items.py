# -*- coding: utf-8 -*-

import scrapy


class CourseImagesItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()


class MultipageCourseItem(scrapy.Item):
    name = scrapy.Field()
    image = scrapy.Field()
    author = scrapy.Field()


class FollowspiderItem(scrapy.Item):
    pass
