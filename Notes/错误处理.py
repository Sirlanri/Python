#try
try:
    print('try ')
    r=2/0   #出错直接跳转到except语句
    print('result:',r)
except ZeroDivisionError as e:#出错类型
    print('except:',e)
finally:
    print('最后')
print('结束')

def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2

try:
    bar(0)
except Exception as e:
    print('\n出错啦！',e)
finally:
    print('结束_(:з」∠)_')

#调用栈
class makedeath(object):
    name=''
    producer=''
    num=00000
    def setname(self,name):
        if isinstance(name,str):
            self.name=name
        else:
            print('输入字ok？')
    def dele(self):
        del self
se=makedeath()
se.setname('woshi')
print(se.name)