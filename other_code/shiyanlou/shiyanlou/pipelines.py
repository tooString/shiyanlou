# -*- coding: utf-8 -*-

from sqlalchemy.orm import sessionmaker
from shiyanlou.models import Course, User, engine
from scrapy.exceptions import DropItem
from datetime import datetime
from shiyanlou.items import CourseItem, UserItem

class ShiyanlouPipeline(object):

    def process_item(self, item, spider):
        '''parse 出来的item 会被传到这里，
        这里编写的处理代码会作用到每一个item上面。
        这个方法必须要返回一个item对象。
        '''
        if isinstance(item, CourseItem):
            self._process_course_item(item)
        else:
            self._process_user_item(item)
        return item

    def _process_course_item(self, item):
        item['students'] = int(item['students'])
        if item['students'] < 1000:
            '''对于不需要的item raise DropItem 异常'''
            raise DropItem('Course student less than 1000.')
        else:
            self.session.add(Course(**item))

    def _process_user_item(self, item):
        item['level'] = int(item['level'][1:])
        item['join_date'] = datetime.strptime(item['join_date'], '%Y-%m-%d').date()
        item['learn_courses_num'] = int(item['learn_courses_num'])
        self.session.add(User(**item))

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
