# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import UserItem

class UsersSpider(scrapy.Spider):
    name = 'users'
    start_urls = ['']

    @property
    def start_urls(self):
        return ('https://www.shiyanlou.com/user/{}/'.format(i) for i in range(525000, 5000, -10))

    def parse(self, response):
        yield UserItem({
            'name': response.xpath('//span[@class="username"]/text()').extract_first(),
            'join_date': response.xpath('//span[@class="join-date"]/text()').re_first('[\d-]*'),
            'status': response.xpath('//div[@class="userinfo-banner-status"]/span[1]/text()').extract_first(),
            'job': response.xpath('//div[@class="userinfo-banner-status"]/span[2]/text()').extract_first(),
            'school': response.xpath('//div[@class="userinfo-banner-status"]/a/text()').extract_first(),
            'type': response.xpath('//a[@class="member-icon"]/img[@class="user-icon"]/@title').extract_first('普通用户'),
            'level': response.xpath('//span[@class="user-level"]/text()').extract_first(),
            'learn_courses_num': response.xpath('//span[@class="latest-learn-num"]/text()').extract_first()
        })
