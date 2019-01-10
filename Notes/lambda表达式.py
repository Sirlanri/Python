#lambda是‘小函数’，只可以包含一个表达式，表达式的计算结果相当于返回值

f=lambda x,y,z:x+y+z
print(f(1,2,3))#把lambda当做函数

g=lambda x,y=3,z=3:x+y+z#有初始值的参数
print(g(1))
print(g(2,y=1,z=1))#关键参数带入

l=[(lambda x:x**2),(lambda x:x**3),(lambda x:x**4)]#数列的形式
print(l[0](2),l[1](2),l[2](2))#引用数列的位置[]

d={'f1':(lambda:2+3),'f2':(lambda:2+4)}
print(d['f1'](),d['f2']())

h=range(11)
print(*map((lambda i:i+10),h))#作为函数表达式 无*会输出地址，书中错误地删去了*

def han(n):#自定义乘方函数
    return n**2
a=range(1,6)
print(*map((lambda x :han(x)),a))#把一个数列导入函数

date=list(range(20))
import random
random.shuffle(date)#随机排序
print(sorted(date,key=lambda x:x))#按大小排序
print(sorted(date,key=lambda x:x,reverse=1))#反向输出
print(sorted(date,key=lambda x:(str(x))))#按照str排序
