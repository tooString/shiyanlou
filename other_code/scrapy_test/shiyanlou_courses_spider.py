import scrapy


class ShiyanlouCourseSpider(scrapy.Spider):
    name = 'shiyanlou-courses'

    @property
    def start_urls(self):
        url_tmpl = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
        return (url_tmpl.format(i) for i in range(1, 23))

    def parse(self, response):
        for course in response.xpath('//div[@class="course-body"]'):
            yield {
                'name': course.xpath('.//div[@class="course-name"]/text()').extract_first(),
                'desc': course.xpath('.//div[@class="course-desc"]/text()').extract_first(),
                'type': course.xpath('.//div[@class="course-footer"]/span[contains(@class, "pull-right")]/text()').extract_first(default='免费'),
                'students': course.xpath('.//span[contains(@class, "pull-left")]/text()[2]').re_first('[^\d]*(\d*)[^\d]*')
                }
