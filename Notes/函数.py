#python里的自定义函数

def fei(n):#计算斐波那契数列
    a,b=1,1
    for x in range(n):
        a,b=b,a+b
    print(b)

fei(10)#调用函数

#关键参数
def guan(a,b,c=5):
    print(a,b,c)
guan(3,2)#只传递ab
guan(3,2,1)#可以改写c值
guan(a=1,b=2,c=3)
guan(b=5,a=6,c=7)#可以打乱顺序,无视位置


#可变长度参数
def kebian(*p):#将接收的任意多的实参放到一个元组内
    print(p)
kebian(1,2,3)

def kebian2(**p):#接收类似于关键参数一样的显示赋值形式的多个实参并将其放入字典中
    for item in p.items():
        print(item)
kebian2(x=1,y=2,z=3)


#序列解包
def jie(a,b,c):
        print(a+b+c)
x=[1,2,3]
jie(*x)#直接把列表带入到函数
y=(1,2,3)#元组
jie(*y)
z={1:'a',2:'b',3:'c'}#字典
jie(*z)#默认使用字典的‘键位’
jie(*z.values())#通过values调用字典的值 