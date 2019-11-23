# 6.1生成随机密码
from random import *
import collections

record_num=[]

def rancre():
    mi = ''
    for i in range(8):
        n = randint(0, 62)
        if 0 <= n <= 9:
            mi = mi+chr(n+48)  # str(0`9)
        elif 10 <= n <= 35:
            mi = mi+chr(n+55)
        elif 36 <= n <= 61:
            mi = mi+chr(n+61)

    if len(mi)<8:
        record(n)
    return mi


def main():
    for i in range(1, 1000):
        rancre()
        #print("生成的第{}个密码是:{}".format(i, rancre()))
    for num in record_num:
        print(num)    
    print(collections.Counter(record_num))

def record(num):
    record_num.append(num)

main()  # 上面是定义了2个函数，这个main()才是执行
