# MariaDB

修改字段约束:

```Mysql 
alter table table_name modify column_name varchar(64) unique;
alter table user add constraint unique(email);
```

MySQLdb模块报错:

​	`pip3 install mysqlclient`

Create_engine

​	dialect[+driver]://user:password@host/dbname[?key=value..]

```Mysql 
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Table, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

engine = create_engine('mysql://root:5241@localhost/shiyanlou')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
```

```Mysql 
class User(Base):
         __tablename__ = 'user'
    
         id = Column(Integer, primary_key=True)
         name = Column(String)
         email = Column(String)
    
         def __repr__(self):
             return "<User(name=%s)>" % self.name 
```

```Mysql 
class Course(Base):
         __tablename__ = 'course'
    
         id = Column(Integer, primary_key=True)
         name = Column(String)
         teacher_id = Column(Integer, ForeignKey('user.id'))
         teacher = relationship('User')
     
         def __repr__(self):
             return '<Course(name=%s)>' % self.name
```

```Mysql 
class Lab(Base):
        __tablename__ = 'lab'
    
        id = Column(Integer, primary_key=True)
        name = Column(String(64))
        course_id = Column(Integer, ForeignKey('course.id'))
        course = relationship('Course', backref='labs')
    
        def __repr__(self):
             return '<Lab(name=%s)>' % self.name
```

```Mysql 
class UserInfo(Base):
         __tablename__ = 'userinfo'
    
         user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
         addr = Column(String(512))
    
```

```Mysql
course_tag = Table('course_tag', Base.metadata,
         Column('course_id', ForeignKey('course.id'), primary_key=True),
         Column('tag_id', ForeignKey('tag.id'), primary_key=True)
     )
```

```Mysql 
class Tag(Base):
          __tablename__ = 'tag'
          id = Column(Integer, primary_key=True)
          name = Column(String(64))
     
          courses = relationship('Course',
                                 secondary=course_tag,
                                 backref='tags')
     
          def __repr__(self):
              return '<Tag(name=%s)>' % self.name
```

```Mysql 
Base.metadata.create_all(engine)
```

