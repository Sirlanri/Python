#实验指导书，实验四，求素数
import math,numpy

max=100
#max=int(input('输入自然数~'))
for i in range(1,max):
    flag=True
    for j in range(2,int(math.sqrt(i)+2)):#这里为啥+2？？？数学问题=-=
        if i%j==0:
            flag=False
            break
    if flag:
        print(i)