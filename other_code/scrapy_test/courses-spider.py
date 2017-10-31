
import scrapy


class ShiyanlouCoursesSpider(scrapy.Spider):
    name = 'shiyanlou-courses'

    def start_requests(self):
        # 课程列表页面 url 模版
        url_tmpl = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
        # 所有要爬取的页面
        urls = (url_tmpl.format(i) for i in range(1, 23))
        # 返回一个生成器，生成 Request 对象，生成器是可迭代对象
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
    # 遍历每个课程的 div.course-body
        for course in response.css('div.course-body'):
            # 使用 css 语法对每个 course 提取数据
            yield {
                # 课程名称
                'name': course.css('div.course-name::text').extract_first(),
                # 课程描述
                'description': course.css('div.course-desc::text').extract_first(),
                # 课程类型，实验楼的课程有免费，会员，训练营三种，免费课程并没有字样显示，也就是说没有 span.pull-right 这个标签，没有这个标签就代表时免费课程，使用默认值 `免费｀就可以了。
                'type': course.css('div.course-footer span.pull-right::text').extract_first(default='免费'),
                # 注意 // 前面的 .，没有点表示整个文档所有的 div.course-body，有 . 才表示当前迭代的这个 div.course-body
                'students': course.xpath('.//span[contains(@class, "pull-left")]/text()[2]').re_first('[^\d]*(\d*)[^\d]*')
            }
