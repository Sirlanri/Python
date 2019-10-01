#比赛的几个题，顺手做一下，做到自闭_(:з」∠)_
import time
def qiuhe(num1,num2):
    fen=[]
    result=0
    for i in range(num1,num2+1):
        fen.append(i)
    for j in fen:
        result+=int(j)
    return result

def qiuhe2(num1,num2):
    fen=[]
    sum=0
    for i in range(num1,num2+1):
        i=str(i)
        for j in range(len(i)):
            fen.append(int(i[j]))
    for i in fen:
        sum+=i
    print(sum)

kong=''
def wenjian1(path):
    global kong
    import os
    all=os.listdir(path)
    
    for item in all:
        if os.path.isdir(item):
            print('kong','+--',item)
            wenjian1(item)
        else:
            print('kong','--',item)

def tiaohe():
    n=1
    min=0.0
    count=1
    clock=time.clock()
    while 1:
        for i in range(100000):
            min+=1.0/n
            n+=1
        end=time.clock()
        print('第{}W，和{}，用时{}'.format(count*10,min,end-clock))

        count+=1
#在web端的修改