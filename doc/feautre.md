# 高级特性

1. 高阶函数：
    * 可以把函数作为参数传入，并利用传入的函数对数据进行处理
    * map filter lambda
    * 示例代码：
    
    ```
    >>> numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> f = filter(lambda x: x % 2 == 0, numbers)
    >>> m = map(lambda x: x * x, numbers)
    ```
2. 迭代器：
    * 能用next函数不断的去获取它的下一个值，直到迭代器返回StopIteration异常。
    * 所有的可迭代对象都可以通过iter函数去获取它的迭代器。
生成器：
    * 生成器是一个迭代器，但是生成器只能被迭代一次。再次迭代，不会打印元素也不会报错
    * 生成器不把所有元素存在内存，动态生成。
3. yield：
    yield返回一个生成器。
    示例代码:
	
	```
    def fib(n):
        current = 0
        a, b = 1, 1
        while current < n:
            yield a
            a, b = b, a + b
            current += 1
   ``` 
    使用yield的函数，执行到yield返回一个元素。
    再次迭代生成器，从yield后面继续执行，直到遇到下一个yield或函数结束退出。
    
    ```
    [x for x in fib(1)] >> [1]
    [x for x in fib(2)] >> [1, 1]
    [x for x in fin(3)] >> [1, 1, 2] ...
    ```
4. 装饰器：
    可以为一个函数添加额外的功能而不影响函数的主体功能。
    本质上是一个函数，接受一个函数作为参数。
    示例代码：
	
	```
	from datetime import datetime
	def log(func):
	    def decorator(*args, **kwargs):
	        print('Function ' + func.__name__ + ' has been called at ' + \ 
	           datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
	        return func(*args, **kwargs)
	    return decorator
	
	@log
	def add(x, y):
	    return x + y
	
	add(1, 2)
	Function add has been called at 2017-08-29 13:11:48
	3
    ```
    @log add()  和 add = log(add) 等同 add变成log函数的返回函数decorator
    可以在装饰函数log中使用@wraps(func)解决(functools.wraps)


