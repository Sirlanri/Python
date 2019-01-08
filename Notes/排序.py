x=list(range(20))
import random#引入函数
random.shuffle(x)#随机排序
print('随机排序',x)
x.reverse()#逆向排序
print('逆向排序',x)
x.sort()#sort 默认是按照大小排序
print('正向排序',x)
x.sort(key=str)#按照字符串排序
print('str排序',x)
#sort 和reverse是直接对原列表操作，原数据全部丢失
random.shuffle(x)#随机排序
y=sorted(x)#sorted不改变原函数
print('新数列默认排序',y)
y=sorted(x,key=str)#字符排序
print('新函数字符排序',y)
y=reversed(x)#倒序
print('新函数倒序',y)
y=sorted(x)
y.reverse()
print('倒序数列',y)
print('-------------------')

result=[['rico',80,'a'],['sirlan',99,'b'],['wallence',71,'d'],['rex',62,'a'],
['sukura',55,'a'],['coldplay',36,'a']]
from operator import itemgetter
r2=sorted(result,key=itemgetter(1))#按照第二项（分数）排序
print('分数排序',r2)
r3=sorted(result,key=itemgetter(2,1))#先第三项排序，然后第二项排序
print('等级+分数',r3)
print('等级+分数倒序',list(reversed(r3)))
r4=sorted(result,key=itemgetter(2,0))#第三项，然后第一项
print(r4)
#r5=sorted(result,key=lambda item:(len(itemgetter(0)))) #出错

print('----------------------')
x=list(range(10))
import random
random.shuffle(x)#随机排序
print('随机排序',x)
print('最大值',max(x))
print('最小值',min(x))
print('总和',sum(x))
print('列表元素个数',len(x))
m=[1,2,3,4]*3#列表每个数与3相乘,不会更改原列表
print(m)
print([1,2,3]+[4,5,6])#函数相加（融合）,生成新列表

list1=[i*i for i in range (10)]
print(list1)
b=sum([i**i for i in range(64)])
#print(b)

c=[(x,y) for x in range(3) for y in range(4) if x!=y]#计算复杂的数组
print(c)

c=[]#上面数组的分步骤
for x in range(10):
    for y in range(20):
        if x==y:
            c.append((x,y))
print(c)
