class line(object):
    a=[]
    def put (self,x):
        self.a.append(x)
    def out (self):
        self.a.pop(0)
    def show(self):
        print(self.a)

from queue import Queue
q=Queue()
q.put(0)#在队尾插入元素
q.put(1)
q.put(2)
print(q.queue)#查看所有元素
print(q.get())#返回然后删除首部元素

#优先级队列
from queue import PriorityQueue
q=PriorityQueue()
q.put(3)
q.put(100)
q.put(8)
print(q.queue)#查看所有元素
q.put(5)
q.put(1)
q.get()#输出并删除最小值

#双端队列
from collections import deque
q=deque([1,2,3,4,5])
q.append(20)#默认加到队列右边
q.appendleft(0)#加到左边
q.pop()#默认返回删除最右
q.popleft()#左边
print(q)#直接输出