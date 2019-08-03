from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep
import threading

#多进程
def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))

def main1():
    start = time()
    p1 = Process(target=download_task, args=('Python从入门到住院.pdf', ))
    p1.start()
    p2 = Process(target=download_task, args=('Peking Hot.avi', ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


#另一种更好的方式 多线程

def download(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(1, 3)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))

def main2():
    start = time()
    t1 = Thread(target=download, args=('Python从入门到住院.pdf',))
    t1.start()
    t2 = Thread(target=download, args=('Peking Hot.avi',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.3f秒' % (end - start))

#为啥我看不懂...我自己重写一个吧
def myselfTesk(num):
    print('第{}个任务开始运行'.format(num))
    print('第{}个运行结束'.format(num))

def mainMy():
    for i in range(10):
        print('第{}个循环开始啦~'.format(i+1))
        selfTesk=Thread(target=myselfTesk,args=(i+1,))
        selfTesk2=Thread(target=myselfTesk,args=(i+11,))
        selfTesk.start()
        selfTesk.join()
        selfTesk2.start()
        selfTesk2.join()
        
        print('第{}个循环结束啦~\n\n'.format(i+1))

#锁线程，保证变量可以被正确修改（差不多这意思吧
class Bank:
    balance=0
    def __init__(self):
        xc=threading.Thread(target=self.change,args=(1,))
        xc2=threading.Thread(target=self.change,args=(2,))
        xc.start()
        xc.join()
        xc2.start()
        xc2.join()
        

    def change(self,num):
        for i in range(1000):
            threading.Lock.acquire()
            balance+=1
            threading.Lock.release()
        print('第{}计算完毕，结果是{}'.format(num,balance))

bank=Bank()