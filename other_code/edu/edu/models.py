# -*- coding: utf-8 -*-

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()


class Base(db.Model):
    ''' 所有 model 的一个基类，默认添加了时间戳
    '''
    # 不要把这个类当成 model
    __abstract__ = True

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class User(Base, UserMixin):
    __tablename__ = 'user'

    # 用数字表示角色，方便判断是否有权限
    ROLE_USER = 10
    ROEL_STAFF = 20
    ROEL_ADMIN = 30

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, index=True, nullable=False)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    # sqlalchemy 默认用字段名做列名，这里指定列名为password
    _password = db.Column('password', db.String(256), nullable=False)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    job = db.Column(db.String(64))
    publish_courses = db.relationship('Course')

    def __repr__(self):
        return '<User:{}>'.format(self.username)

    @property
    def password(self):
        ''' Python 风格的 getter
        '''
        return self._password

    @password.setter
    def password(self, orig_password):
        ''' Python 风格的 setter
        user.password 会自动为 password 生成哈希值存入 _password 字段
        '''
        self._password = generate_password_hash(orig_password)

    def check_password(self, password):
        ''' 判断用户输入的密码和存储的 hash 密码是否相等
        '''
        return check_password_hash(self._password, password)

    @property
    def id_admin(self):
        return self.role == self.ROEL_ADMIN

    @property
    def is_staff(self):
        return self.role == self.ROEL_STAFF


class Course(Base):
    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, index=True, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    author = db.relationship('User', uselist=False)
