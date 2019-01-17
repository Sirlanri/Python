class stu(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            print('输入数字')
        elif not 0<=value<=100:
            print('成绩无效')
        else:
            self._score=value
s=stu()
s.score=60#实际转化为s.set_score(60)
print(s.score)

#只定义getter方法，不定义setter方法就是只读属性：
class screen(object):
    @property
    def wide(self):
        return self._wide
    @wide.setter
    def wide(self,value):
        if value<9999:
            self._wide=value
    @property
    def reso(self):
        self.reso=5000
p=screen()
p.wide=20

#正确源码
class C(object):
    def __init__(self): self._x = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
c=C()
c.x=20