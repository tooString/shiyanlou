# -*- coding: utf-8 -*-
import scrapy
from followspider.items import CourseImagesItem


class CoursesImageSpider(scrapy.Spider):
    name = 'courses_image'
    start_urls = ['https://www.shiyanlou.com/courses/']

    def parse(self, response):
        item = CourseImagesItem()
        item['image_urls'] = response.xpath('//div[@class="course-img"]/img/@src').extract()
        yield item
