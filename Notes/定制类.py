#__xxx__是有特殊定义的

#str
class student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):#使其返回姓名的字符串
        return 'student object (name:%s)'% self.name
print(student('jack'))
s=student('a')
s.name='fuckkkk'
print(s.name)

#iter,类似for循环,与__next__搭配使用
class fib (object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self #实例本身就是跌送对象，所以返回自己
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b#斐波那契
        if self.a>10000:
            raise StopIteration()#遇到这个时停止循环
        return self.a 
#把fib实例作用于for循环
for n in fib():
    print(n)

#实现下标取元素，用getitem
class fib2(object):
    def __getitem__(self,n):
        a,b=1,1
        for i in range(n):
            a,b=b,a+b
        return a
f=fib2()
for x in range(20):
    print(f[x])#可以通过下标访问任意一项
#使用切片
class qie(object):
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b=1,1 
            for x in range(n):
                a,b=b,a+b
            return a
        if isinstance(n,slice):#如果n是切片
            start=n.start
            stop=n.stop
            if start is None:
                start=0
            a,b=1,1
            l=[]
            for x in range(stop):
                if x>=start:
                    l.append(a)
                a,b=b,a+b
            return l
q=qie()
print(q[3:20])

#输出不存在的属性getattr
class st(object):
    def __init__(self):#并没有定义score
        self.name='sirlan'
    def __getattr__(self,attr):
        if attr=='score':#如果请求score，就返回100
            return 100
sir=st()
print(sir.score)#直接输出了100
