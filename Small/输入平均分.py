num=[]
while 1:
    x=int (input('输入分数'))
    if x==0:
        break
    num.append(x)
print(sum(num)/len(num))