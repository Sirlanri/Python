class Car():
    def __init__(self, make='china',model='普通型',year='2019'):
        self.make=make
        self.model=model
        self.year=year
        self.meter=0
    def getname(self):
        name=self.make+' '+self.model+' '+str(self.year)
        return name
    def readmeter(self):
        return self.meter
    def upedate(self,new):
        if new>0:
            self.meter+=new
        else:
            print('输入数据不合法')
class battery(Car):
    def __init__(self, make='china',model='普通型',year='2019',battery=60):
        super().__init__(make,model,year)
        self.battery=battery
    def readbat(self):
        print('电池容量是:{}'.format(self.battery))