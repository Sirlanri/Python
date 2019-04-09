#为被装饰的调用点字符串附加一个字符串
def decorated(func):
    func.__doc__+='\n添加的字符串\n'#修改了doc属性
    return func
def add(x,y):
    return x+y
add=decorated(add)#将装饰器应用到函数上

@also_decorated
@decorated0
def add2(x,y):
    return x+y#将return的值返回给@also_decorated
