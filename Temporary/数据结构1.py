class ShunXu:
    '''有三个变量——num，name，price'''

    def __init__(self, num='', name='', price=0):
        self.num = num
        self.name = name
        self.price = price

    @property
    def infor(self):
        return self.name+self.num+str(self.price)

    @infor.setter
    def infor(self, name, price):
        self.num = num
        self.name = name
        self.price = price


class SX_list2():  # 顺序表2号
    '''一个线性顺序列表'''

    def __init__(self):
        # 初始化
        self.list = []

    def insert(self, item):
        '''插入一个元素，必须是同类型'''
        if isinstance(item, ShunXu):
            self.list.append(item)
            print('成功插入')
        else:
            print('类型错误')

    def lookfor(self, num='', name='', price=0):
        '''查找元素，可以传入三个变量的任意一个或多个'''
        # item为结构体类
        for item in self.list:
            if num == item.num or name == item.name or price == item.price:
                print('编号{0}，名字{1}，价格{2}'.format(item.num, item.name, item.price))
            else:
                print('没有查找到')

    def delit(self, num='', name='', price=0):
        '''删除指定元素，可以传入三个变量的任意一个或多个'''
        count = 0
        for item in self.list:
            if num == item.num or name == item.name or price == item.price:
                self.list.remove(count)
            else:
                print('没找到这个元素')
            count += 1


def test1():
    list1=SX_list2()

    cplus=ShunXu('12346','C++入门到入坟',30)
    java=ShunXu('654231','Java从看懂到看开',50)
    py=ShunXu('233333','Python世界第一',99)

    #将元素添加到list
    list1.insert(cplus)
    list1.insert(java)
    list1.insert(py)
    
    #查找测试
    list1.lookfor(num='233333')
test1()