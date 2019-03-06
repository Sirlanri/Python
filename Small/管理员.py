class user(object):
    def __init__(self,name):
        self.name=name
        self.permiss=['read file','liten music']#这里必须用self.
    def display(self):
        print(self.permiss)
    def change(self,new):
        self.permiss.append(new)
        print('添加成功')
class admin1(user):
    def __init__(self, name):
        super().__init__(name)
        self.permiss.append('delete files')
class admin2(user):
    def __init__(self, name):
        super().__init__(name)
        self.permiss.append('web')

girl=user('girl')
girl.display()
boy=admin1('boy1')
boy.display()
boy2=admin2('boy2')
boy2.display()
