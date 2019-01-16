class zhidu:
    def __init__(self,value):
        self.__value=value+1#私有数据成员
    @property#修饰器，私有属性
    def value(self):#只读属性
        return self.__value
z=zhidu(3)
print(z.value)  
z.v=5#可以添加新成员
print(z.v)

class bandel:
    def __init__(self,v):
        self.__v=v
    def __get(self):#读
        return self.__v
    def __set(self,v):#写
        self.__v=v
    v=property(__get,__set)#指定相应的读写方程
    def show(self):
        print(*self.__v)#显示
b=bandel(1)
b2=bandel(2)
print(b.v)
b.v=5#修改值
print(b.v)
print(b2.v)

class all:#可读写删
    def __init__(self,v):
        self.__v=v
    def __get(self):
        return self.__v
    def __writer(self,new):
        self.__v=new
    def __del (self):
        del self.__v
    v=property(__get,__writer,__del)
    def show(self):
        print(self.v) 
t=all(25)
print(t.v)
t.show()#show是公有的，可以直接读取
