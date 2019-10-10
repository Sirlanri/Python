import math,numpy

def liebiao():
    #实验指导书，实验四，列表法求素数
    max=100
    #max=int(input('输入自然数~'))
    for i in range(1,max):
        flag=True
        for j in range(2,int(math.sqrt(i)+2)):#这里为啥+2？？？数学问题=-=
            if i%j==0:
                flag=False
                break
        if flag:
            print(i)

def shaxuan():
    #这个不太明白，直接放弃
    max=input('输入一个大于2的整数')
    numbers=set(range(2,max))
    gen=int(max**0.5)+1
    primesLessThanM = [p for p in range(2, m) if 0 not in [p%d for d in range(2, int(p**0.5)+1)]]
    # 遍历最大整数平方根之内的自然数 
    for p in primesLessThanM: 
        for i in range(2, maxNumber//p+1): # 在集合中删除该数字所有的倍数 numbers.discard(i*p)
            print(numbers)
    
def cni(n,i):
    minNI = min(i, n-i)
    result = 1
    for j in range(0, minNI):
        result = result * (n-j) // (minNI-j)
    print(result)
cni(3,2)