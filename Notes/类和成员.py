#用class关键字来定义类，class+空格+（类名称）
class Car(object):
    def infor(self):
        print('这是车')
car=Car()#实例化对象
print(car.infor())#调用对象的方法
#用isinstance(对象,类)来测试一个对象是不是某个类的实例
class a:
    pass
def b():
    pass
if 1>2:
    pass#pass表示空语句

class c:
    def __init__(self,value1=0,value2=0):
        self._value1=value1#构造函数
        self.__value2=value2#类内部可以访问私有成员
    def setValue(self,value1,value2):#成员方法
        self._value=value1
        self._value=value2
    def show(self):
        print(self._value1)
        print(self.__value2)
d=c()#可以访问类公有成员
print(d._value1)

class Bus(object):
    price=10000#属于类的数据成员
    def __init__(self,c):
        self.color=c#属于对象的数据
car1=Bus('red')
car2=Bus('blue')#我感觉这玩意有点像C语言里的结构体_(:з」∠)_
print(car1.color,car2.price)
Bus.price=999#修改类的属性
Bus.name='double decker'#增加类的类型 
car2.color='green'#更改
print(car1.price,car2.color,Bus.name)
def setSpeed(self,s):#不明白这个函数是干啥的=-=
    self.speed=s
    import types
    car1.setSpeed=types.MemberDescriptorType(setSpeed,car1)#动态为对象增加成员方法
    car1.setSpeed(50)

class Root:
    __total=0
    def __init__(self,v):
        self.__value=v
        Root.__total+=1
    def show(self):#普通实例方法
        print('self.__value:',self.__value)
        print('Root.__total:',Root.__total)
    @classmethod#修饰器，声明类方法
    def classShowTotal(cls):
        print(cls.__total)
    @staticmethod
    def staticShowTotal():
        print(Root.__total)
r=Root(3)
print(r.classShowTotal())#调用类方法
print(r.staticShowTotal())#调用静态方法
print(r.show())
print(Root.classShowTotal())#通过类名调用类方法
print(Root.staticShowTotal())#通过类名调用静方法
