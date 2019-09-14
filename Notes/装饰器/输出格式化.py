#接受Python序列，将其序列化为json格式的装饰器
import functools
import json

def json_output(decorated):
    '''运行装饰功能，把功能的结果连续写入json中，然后返回json的字符串'''
    def inner(*args,**kwargs):
        result=decorated(*args,**kwargs)
        return json.dumps(result)
    return inner
#将装饰器应用到函数
@json_output
def do():
    return [1,23,4,5]
print(do())#输出了有效的json字符串

class jsonError(Exception):
    def __init__(self,message):
        self.message=message
    def __str__(self):
        return self.message
        