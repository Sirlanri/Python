class ShunXu:

    def __init__(self,num='',name='',price=0):
        self.num=num
        self.name=name
        self.price=price
    
    @property
    def infor(self):
        return self.name+self.num+str(self.price)

    @infor.setter
    def infor(self,name,price):
        self.num=num
        self.name=name
        self.price=price


class SX_list1(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def cutin(self,sx):
        self.append(sx)