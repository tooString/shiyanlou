# -*- coding: utf-8 -*-
from ch11_getgithubinfo.models import Repository, engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime


class Ch11GetgithubinfoPipeline(object):
    def process_item(self, item, spider):
        item['update_time'] = datetime.strptime(item['update_time'],
                                                '%Y-%m-%dT%H:%M:%SZ')
        self.session.add(Repository(**item))
        return item

    def open_spider(self, spider):
        '''当爬虫被开启的时候调用
        创建数据库 session
        '''
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        '''当爬虫被关闭时调用
        提交session 然后关闭 session
        '''
        self.session.commit()
        self.session.close()
