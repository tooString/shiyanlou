# -*- coding: utf-8 -*-
import scrapy
from ch11_getgithubinfo.items import GetgithubinfoItem


class RepositorSpider(scrapy.Spider):
    name = 'repositor'

    @property
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1, 5))

    def parse(self, response):
        for repo in response.css('li.source'):
            item = GetgithubinfoItem({
                'name': repo.xpath('.//a[@itemprop="name codeRepository"]/\
                                   text()').re_first("\n\s*(.+)"),
                'update_time': repo.xpath('.//relative-time/@datetime'
                                          ).extract_first()
            })
            yield item
