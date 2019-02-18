import os
import random

os.chdir(r'E:\代码\Python文件操作')

with open('plan.txt','w')as f:
    #生成日期time
    x=1
    y=11
    while 1:
        if x>=2 and y>=25:
            break
        if y==31:
            x=2
            y=1
        time=str(x)+'月'+str(y)+'日'
        y+=1
        #单词
        if y==4 or y==7 or y==17:
            word='没有'
        else:
            word='百词斩40个'
        #听力+朗读
        ran=random.randint(0,9) #随机判断
        if ran==9:
            listen='没听'
        elif ran<2:
            listen='TED演讲'
        elif 2<ran <=8:
            listen='CBC News'
        else:
            listen='CBC+TED'
        #其他
        other='Twitter'
        if ran>4:
            other='BBC(English)+Twitter'
        all=time+'  单词:'+word+'   听力：'+listen+'    '+'其他：'+other+'\n'
        print(all)
        other=''
        f.write(all)
    f.close()