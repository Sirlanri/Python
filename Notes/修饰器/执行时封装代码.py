def requires_ints(decorited):
    def inner(*args,**kwargs):
        #获得键盘输入的全部数据
        kwarg_values=[i for i in kwargs.values()]
        for arg in list(args)+kwarg_values:
            if not isinstance(arg,int):
                raise TypeError('{}只能使用int类型数据'.format(decorited.__name__))
        #运行修饰器，返回结果
        return decorited(*args,**kwargs)
    return inner

@requires_ints
def foo(x,y):
    '''返回xy的和'''
    return x+y
print(foo(3,4))