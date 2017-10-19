
# 多进程

###### Process类封装多进程操作
        p = Process(target=hello, args=('shiyanlou', ))
        p 是一个用Process定义的子进程对象。执行hello函数，传入参数'shiyanlou'。
        p.start()   调用start()方法，启动子进程。调用hello函数，传参。
        p.join()    等待子进程运行结束后继续执行。

###### Pipe 和 Queue 实现进程间的数据交换

###### Pipe() 管道
返回一个tuple 写入数据用send 读取数据用recv

    
```
    from multiprocessing import Process, Pipe

    conn1, conn2 = Pipe()

    def f1():
        conn1.send('Hello shiyanlou')

    def f2():
        data = conn2.recv()
        print(data)

    def main():
        Process(target=f1).start()
        Process(target=f2).start()

    if __name__ == '__main__':
        main()

```
    f1 用 send 向pipe管道写入字符串
    f2 用 recv 从管道中接收字符串
    在main中 创建的两个进程。执行main 输出字符串

###### Queue队列结构
    
    
```
    from multiprocessing import Process, Queue

    queue = Queue()

    def f1():
        queue.put('Hello shiyanlou')

    def f2():
        data = queue.get()
        print(data)
```
    put 传送字符串
    get 接收字符串
    queue = Queue(maxsize=10) 初始化时制定最大容量

###### 进程同步：
    多进程的推进顺序无法预测
    在对一个变量进行操作的时候，为变量加一把锁，当前进程操作此变量，其他进程不能操作它。
    Lock：使用acquire 获取锁 release 释放锁

    
```
    import time
    from multiprocessing import Process, Value, Lock

    def func(val, lock):
        for i in range(50):
            time.sleep(0.01)
            # with lock 语句是对下面语句的简写：
            
            # lock.acquire()
            # val.calue += 1
            # lock.release()
            
            with lock:
                val.value += 1

    if __name__ == '__main__':

        v = Value('i', 0)
        ＃ 初始化锁
        lock = Lock()
        procs = [Process(target=func, args=(v, lock)) for i in range(10)]
        #当一个子进程结束后，下个子进程才能操作变量i

        for p in procs:
            p.start()
        for p in procs:
            p.join()

        print(v.value)

```
###### 进程池Pool：
    预设若干进程进进程池，有任务，从池中去一个进程执行任务，完成后返回进程池。
    有新任务，而进程池中没有进程，新任务得等到某个进程执行完才能执行。

