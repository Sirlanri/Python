#设计自定义栈
class zhan():
    a=[]
    y=len(a)-1#y是数列的个数(坐标)
    def putin(self,x):
        if isinstance(x,int):
            self.a.append(x)
        elif isinstance(x,list):
                for i in range(len(x)):
                    self.a.append(x[i])
        else:
            s=x.split(" ")#输入的数字+空格怎么解决？？？
            for i in range(len(x)):
                    self.a.append(s[i])
    def out(self):#输出并删除
        print(self.a[self.y]) 
        del self.a[self.y]
    def kong(self):#清空
        if self.a==[]:
            print('空的啦')
        else:
            self.a=[]
            print('已经清空')
    def change(self,n):#删除指定位后的元素
        if self.y<=n:
            print('不需要改变')
        else:
            for i in range(n-self.y):
                del self.a[self.y]
                if self.y==n:
                    print('完成~~')
    def show(self):
        if self.a==[]:
            print('空的哟')
        else:
            print(self.a)
z=zhan()
z.putin(1)
z.show()