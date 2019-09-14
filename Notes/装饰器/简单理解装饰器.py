#源自廖雪峰博客
def log(func):
    def out(*args,**kw):
        print('现在运行的函数名是：{0}'.format(func.__name__))
        return func(*args,**kw)
    return out()

@log
def now():
    print('时间是')
now#执行函数


#自己写了一个
print('\n\n')
def kkp(func):
    def out(*args,**kw):
        print('这是装饰器内部第二层')
        print('当前运行的是{}'.format(func.__name__))
        return func(*args,**kw)
    print('这是装饰器内部第一层')
    print('zm?kkp?')
    return out()
@kkp
def zzz():
    print('主函数测试啦啦啦')
zzz#直接这样调用？？？？


#自己写了二个_(:з」∠)_
print('\n第二个~')
def zm(func):#这玩意儿竟然也能这样写？
    print('这是装饰器内容')
    return func
@zm
def zm1():
    print('这是函数内容')
zm1

#有点不过瘾，再来一个带参数的_(:з」∠)_
print('\n\n')
def wula(func):
    print('装饰器走起')
    def out(n):
        print('接收到的参数是{}'.format(n))
        return func
    return out
@wula
def lalala():
    print('现在执行的是函数本体')
lalala(2)#这一步只执行了乌拉装饰器内容
lalala(10)()#执行完乌拉修饰器后，执行啦啦啦本体