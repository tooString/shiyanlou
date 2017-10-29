# MongoDB

```MongoDB
启用MongoDB:
mongod --config /usr/local/etc/mongod.conf
brew services start mongodb

use database;
show databases; 	# 显示当前存在的数据库
show collection;	# 显示当前数据库的所有文档集合。
```

插入语句：

```MongoDB
db.collection.insertOne({})
db.collection.insertMany([{},{},{}])
```

查询语句：

```MongoDB
db.collection.find()	# 查询所有用户
db.collection.find({name: "jin"})	# 查询名字为jin的用户
db.collection.find({age: {$gt: 30}})	# 查询年龄大于30的用户
db.collection.fin({addr: "CD"})		# 查询地址包含CD的用户
```

更新数据：

```MongoDB
db.collection.updateOne(
	{name: "Aiden"},
	{$set: {age: 29, addr: ["CD", "SH", "BJ"]}}
	)	# 可以只更新需要改的部分
db.collection.updateMany()
```

删除数据：

```MongoDB
db.collection.deleteOne()
db.collection.deleteMany({addr: "CD"})	# 删除所有地址包含CD的用户
```

