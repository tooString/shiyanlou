import scrapy


class Git_Spider(scrapy.Spider):
    name = 'git_repos'

    @property
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1, 5))

    def parse(self, response):
        for repo in response.css('li.source'):
            yield {
                'name': repo.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first("\n\s*(.+)"),
                'update_time': repo.xpath('.//div[contains(@class, "f6")]/relative-time/@datetime').extract_first()
                }
