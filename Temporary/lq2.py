import math
def kaisa():
    strs = input()
    after = ''
    for single in strs:
        i = ord(single)
        i = ((i + 2)-97)%26+97
        i = chr(i)
        after=after+i
    print(after)

def fanbeishu():
    n = int(input())
    a,b,c = map(int,input().split())
    count = 0
    for i in range(1,n):
        if i%a != 0:
            if i%b != 0:
                if i%c != 0:
                    count+=1
    print(count)

def baidong():
    m,n = map(int,input().split())
    for i in range(math.pow(n,m)):
        i+=1
        pass

baidong()