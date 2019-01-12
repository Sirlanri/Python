#接收实数，返回平均数+大于平均数的
def han(p):
    y=[]
    ave=sum(p)/len(p)
    for x in p:
        if x>ave:
            y.append(x)
    y.insert(0,ave)
    return y
i=[1,2,3,4,5]
print(han(i))

#接收字符串参数，返回第一个元素是大写个数，第二个是小写个数
def bos(p):
    a=b=0
    for c in p:
        if 'a'<=c<='z':
            a+=1
        elif 'A' <=c<='Z':
            b+=1
    return a,b
print(bos('dhuIJW'))

#接收一个list和一个整数k，将k之前逆序，k之后逆序，然后将所有元素逆序
def ni(ls,k):#自己写的切片法
    a=ls[k:0:-1]
    b=ls[:k:-1]
    c=a+b
    c=c[::-1]
    return c
#def ni2(ls,k):#高效切片
    #return list([k:]+ls[:k])  书上代码如此，错误


#接收t，返回斐波那契数列中大于t的第一个数
def fei(t):
    a=b=1
    for i in range(t):
        a,b=b,a+b
        if b>t:
            return b
print(fei(100))

#接收一个list，返回第一个值是最小值，第二个值是最小值的下标
def min(p): #自己写的,果然是习惯了面向过程的啊~
    i=0
    a=10
    for x in p:
        i+=1
        if x<a:
            a=x
    return a,i
print(min([11,55,26,87]))

def min2(p):#书上的方法
    minz=min(p)
    pos=[i for i ,value in enumerate(p) if value==minz]#这他喵的啥玩意儿？
    fin=minz+tuple(pos)
    return fin
print(min2([11,55,26,87]))

#接收一个正偶数，输出两个和为此数的素数
def su(a):
    for y in range(1,a):
        if test(y):
            x=a-y
            if test(y):
                print(x,y)
def test(y):#判断素数
    for i in range(2,y):
        if y%i==0:
            return 0        
    return 1
su(100)

#公约公倍数
def gong(x,y):
    if y<x:
        x,y=y,x#x是小的数
    for i in range(x,0,-1):
        if y%i==0 and x%i==0:
            break   
        t=x 
    while 1:
        if t%y==0:
            break
        else:
            t+=x
    return i,t
print(gong(3,10))
def gong2(m,n):#书上的蜜汁代码
    if m>n:
        m,n=n,m#n是大数
    p=m*n
    while m!=0:#这他喵的什么套路啊！？数学题啊！？
        r=n%m
        n=m
        m=r
    return(n,int(p/n))
print(gong2(3,10))

#比n小的排n前，比n大排n后，快排算法的步骤
import random
def qp(p,n):#这写的太简洁了，好评好评佩服佩服
    l1=[i for i in x if i<n]
    l2=[i for i in x if i>n]
    return l1+[n]+l2
x=list(range(20))
random.shuffle(x)
print(qp(x,9))