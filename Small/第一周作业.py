class homework():
    def gas(self):
        i=1
        miles=gass=0.0
        print("输入0退出程序哟亲~")
        while 1:
            mile=input("输入第"+i+"个英里")
            gas=input("输入第"+i+"个油")
            if gas==0 or mile==0:
                break
            miles+=mile
            gass+=gas
        ave=miles/gass
        print("平均油耗是{}".format(ave))
    
    def max(self):
        a=[]
        for i in range(5):
            a[i]=input("输入第{}个数".format(i))
        a=a.sort()
        print("最大值是{}，最小值是{}".format(a[0],a[4]))

    def sales(self):
        x=y=0.0
        while 1:
            print("输入对应的号码,输入其他号码退出")
            print("1-239.99\n2-129.75\n3-99.95\n4-350.89")
            no=input()
            if no==4:
                x+=350.89
            elif no==1:
                x+=239.99
            elif no==2:
                x+=129.75
            elif no==3:
                x+=99.95
            else:
                break
        y=200.0+0.09*x
        print("工资是{}".format(y))
    
    def password(self):
        a=[]
        b=[]
        for i in range(4):
            a[i]=int(input("输入第{}个数".format(i)))+7
            if a[i]>9:
                a[i]-=10
        b[2]=a[0]
        b[3]=a[1]
        b[1]=a[3]
        b[0]=a[2]
        print(b)