registry=[]
def register(decorated):
    registry.append(decorated)
    return decorated

@register
def foo():
    return 3

@register
def bar():
    return 5

answer=[]
for func in registry:
    answer.append(func())
    
class Registry():
    def __init__(self):
        self.functions=[]
    def register(self,decorated):
        self.functions.append(decorated)
        return decorated
    def run__all(self,*args,**kwargs):
        return_value=[]
        for func in self.functions:
            return_value.append(func(*args,**kwargs))
        return return_value


a=Registry()
b=Registry()

@a.register
def foo(x=3):
    return x

@b.register
def foo(x=5):
    return x

@a.register
@b.register
def baz(x=7):
    return x
