#模拟集合类的运算
class set():
    def __init__(self, data=None):
        if data==None:
            self__data=[]
        else:
            if not hasattr(data,'__iter__'):
                #提供的数据不可迭代，无法实例化
                raise Exception('必须提供可迭代的数据类型')
            temp=[]
            for item in data:
                #集合的数据必须可哈希
                hash(item)
                if not item  in temp:
                    temp.append(item)
            self.__data=temp
    def __del__(self):
        del self.__data
    def add(self,value):
        hash(value)
        if value not in self.__data:
            self.__data.append(value)
        else:
            print('这个元素已经存在了哟')
    #删除元素
    def remove(self,Value):
        if Value in self.__data:
            self.__data.remove(Value)
            print('删除成功')
        else:
            print('元素不存在，无视ing')
    #弹出（并删除）元素
    def pop(self):
        if not self.__data:
            print('已经被清空，无视操作')
            return
        import random
        item=random.choice(self.__data)
        print(item)
        self.__data.remove(item)
    def __sub__(self,Set1):
        if not isinstance(set1,set):
            raise Exception('类型错误')
        #空集合
        result=set()
        for item in self.__data:
            if item not in set1.__data:
                result.__data.append(item)
        return result
    #差运算
    def difference(self,another):
        if not isinstance(another,set):
            raise Exception('类型不对哟')
        return self-another
    #集合并集 | 
    def __or__(self,another):
        if not isinstance(another,set):
            raise('类型不对')
        result=Set(self.__data)
        for item in another.__data:
            if item not in result.__data:
                result.__data.append(item)
        return result
    #并集
    def union(self,num):
        if not isinstance(num,set):
            raise('类型错误啦')
        return self|num
    #交集
    def __and__(self,num):
        result=set()
        for item in self.__data:
            if item in num.__data:
                result.__data.append(item)
            return result
    #两个集合是否相等
    def __ep__(self,num):
        if not isinstance(num,set):
            raise('类型不对呀亲~')
        if sorted(self.__data)==sorted(num.__data):
            return 1
        else:
            return 0
    #包含关系
    def __gt__(self,num):
        if not isinstance(num,set):
            raise Exception('类型不对呀亲！')
        if self!=num:
            flag1=1
            for item in self.__data:
                if item not in num.__data:#当前集合有元素不属于另一个集合
                    flag2=0
                    break
            if not flag1 and flag2:
                return 1
        return 0
    def __ge__(self,num):
        if not isinstance(num,set):
            raise Exception('类型不对呀亲！')  
        return self==num or self>num
    #判断是不是真子集
    def issubset(self,num):
        if not isinstance(num,set):
            raise Exception('不是一个！！！')
        if self<num:#woc原来Python可以这样玩！！？？？
            return 1
        else:
            return 0
    #判断超集
    def issuperset(self,num):
        if not isinstance(num,set):
            raise Exception('不是一个！！！')
        if self>num:#woc原来Python可以这样玩！！？？？
            return 1
        else:
            return 0
    def clear(self):
        #这个删除的思路真是清晰脱俗，学习到了
        while self.__data:
            del self.__data[1]
        print('已经清空')
    #直接查看该类时调用此函数
    def __repr__(self):
        return '{'+str(self.__data)[1:-1]+'}'
    #print输出时调用次函数
    def __str__(self):
        return '{'+str(self.__data)[1:-1]+'}'
        