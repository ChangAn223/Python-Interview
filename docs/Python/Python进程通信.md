## Python进程通信

https://blog.csdn.net/weixin_43790276/article/details/90906683
https://www.cnblogs.com/guguobao/p/9398653.html

### 1. 第一种：Queue
```
from multiprocessing import Queue

Queue([maxsize])

maxsize：指定队列的长度，即队列中消息的最大数量

初始化Queue对象时，若括号中没有指定最大可接收的消息数量，或数量为负值，那么就代表可接受的消息数量没有上限（直到内存的尽头）；

Queue的常用方法：

1.qsize()：返回当前队列包含的消息数量，即当前队列中有多少条数据

2.empty()：如果队列为空，返回True，反之False 

3.full()：如果队列满了，返回True，反之False

4.get([block[, timeout]])：获取队列中的一条消息，然后将其从列队中移除，block默认值为True

如果block使用默认值，且没有设置timeout(单位秒)，列队为空，此时程序将被阻塞（停在读取状态），直到从列队读到消息为止。如果设置了timeout，列队为空，则会等待timeout秒，若还没读取到任何消息，抛出"Queue.Empty"异常。

如果block值为False，消息列队如果为空，则会立刻抛出"Queue.Empty"异常。

5.get_nowait()：相当于Queue.get(False)

6.Queue.put(item,[block[, timeout]])：将item消息写入队列，block默认值为True

如果block使用默认值，且没有设置timeout(单位秒)，列队已满，此时程序将被阻塞（停在写入状态），直到列队腾出空间为止，将数据写入。如果设置了timeout，列队已满，则会等待timeout秒，若还没空间，抛出"Queue.Full"异常。

如果block值为False，消息列队如果没有空间可写入，则会立刻抛出"Queue.Full"异常。

7.Queue.put_nowait(item)：相当于Queue.put(item, False)

```

示例：

```
from multiprocessing import Process, Queue
import time

def put_card(queue):
    """往队列中添加数据"""
    for card in ['A', 'K', 'Q', 'J', '10']:
        print('Put {} to queue...'.format(card))
        queue.put(card)
        time.sleep(1)

def get_card(queue):
    """从队列中取出数据"""
    while True:
        if not queue.empty():
            card = queue.get(True)
            print('Get {} from queue.'.format(card))
            time.sleep(1)
        else:
            break

if __name__ == "__main__":
    q = Queue()
    pp = Process(target=put_card, args=(q,))
    pg = Process(target=get_card, args=(q,))
    pp.start()

    pg.start()
    pg.join()
    print(pg.is_alive())

```

**进程池中的Queue**

如果要使用Pool创建进程，需要使用multiprocessing.Manager()中的Queue()来传递消息。

### 2. 第二种：Pipe

```
from multiprocessing import Pipe

pipe = Pipe()

Pipe常用于两个进程，两个进程分别位于管道的两端
Pipe方法返回（conn1,conn2）代表一个管道的两个端，Pipe方法有duplex参数，默认为True，即全双工模式，若为FALSE，conn1只负责接收信息，conn2负责发送，
send和recv方法分别为发送和接收信息。
```

示例：

```
import multiprocessing
import time, random

# 写数据进程执行的代码
def proc_send(pipe, urls):
    # print 'Process is write....'
    for url in urls:
        print('Process is send :%s' % url)
        pipe.send(url)
        time.sleep(random.random())

# 读数据进程的代码
def proc_recv(pipe):
    while True:
        print('Process rev:%s' % pipe.recv())
        time.sleep(random.random())

if __name__ == '__main__':
    # 父进程创建pipe，并传给各个子进程
    pipe = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=proc_send, args=(pipe[0], ['url_' + str(i) for i in range(10)]))
    p2 = multiprocessing.Process(target=proc_recv, args=(pipe[1],))
    # 启动子进程，写入
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()
```

### 3. 第三种：socket

见网络编程篇




