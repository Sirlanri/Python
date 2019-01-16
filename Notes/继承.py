#设计person类，根据person派生teacher类，分别创建person和teacher类的对象
class Person(object):
    def __init__(self,name='',age=20,sex='man'):
        self.setname(name)
        self.setage(age)
        self.setsex(sex)
    def setname(self,name):
        if not isinstance(name,str):
            print('不合法哟~')
            self.__name=''
            return
        self.__name=name#输入名字
    def setage(self,age):
        self.__age=age
    def setsex(self,sex):
        self.__sex=sex
    def show(self):
        print(self.__name,self.__age,self.__sex)
p=Person('A',31,'feman')
p.show()#一定是p.show()

class Teacher(Person):#从person派生
    def __init__(self,name='',age=30,sex='man',major='math'):#可以不初始化
        super(Teacher,self).__init__(name,age,sex)#初始化私有数据成员
        
        def setmajor(self,major):
            self.__major=major
        def show(self):
            super(Teacher,self).show()#这两个函数没用到...
            print(self.__major)
sirlan=Person('sirlan',18,'secret')
sirlan.show()
zhang=Person('zhang',19,'man')
zhang.show()
susan=Teacher('susan',39,'feman','PE')
susan.show()
susan.setage(40)#用继承的方法修改
susan.show()