a=(1,2,3,4,5)#元组 不可更改
print(a)
zidian={'IP':'8.8.8.8','name':'google','place':'USA'}
print(zidian)
del zidian['place']
print(zidian)
print(zidian.pop('name'))#输出并删除某个键
zidian['place']='Hong Kong'#添加键位和内容
print(zidian['IP'])
print(zidian.get('IP'))
print(zidian.get('name','404'))#若没有name，就返回404

import random
import time
x=list(range(99999))
y=dict(zip(range(99999),range(9999)))
z=10000
start=time.time()
for i in range(9999):
    z in x
print("列表所用的时间是：",time.time()-start)
 
start=time.time()
for i in range(100000):
    z in y 
print("字典所用时间是：",time.time()-start)
