# file 操作 
1. open() 函数需要两个参数，第一个参数是文件路径或文件名，第二个是文件的打开模式。open() 函数返回一个文件对象
    * "r"，以只读模式打开，你只能读取文件但不能编辑/删除文件的任何内容
    * "w"，以写入模式打开，如果文件存在将会删除里面的所有内容，然后打开这个文件进行写入
    * "a"，以追加模式代开，写入到文件中的任何数据将自动添加到末尾
    * "b"，以二进制的方式代开

2. pickle:
    * pickle 将字典序列化成字节（以二进制读取写入）
    * dump 和 load 将字典存入到文件并读取出来恢复成字典 

3. json：
    * json 将字典序列化为字符串
    * dumps 和 loads 执行序列化和反序列化操作

4. os.path:
    * os.path.abspath(path) 返回文件的绝对路径
    * os.path.basename(path) 返回文件名
    * os.path.dirname(path) 返回文件路径
    * os.path.isfile(path) 判断路径是否为文件
    * os.path.isdir(path) 判断路径是否为目录
    * os.path.exists(path) 判断路径是否存在
    * os.path.join(path1[, path2[, ...]]) 把目录和文件名合成一个路径
5. csv
用csv读取一个csv文件

```
    with open('xx.csv') as f:
        for row in csv.reader(f):
            employee_id, salary = row
```

