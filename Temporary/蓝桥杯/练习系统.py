def fshulie(n):
    n=int(input())
    n1=n2=n3=1
    for i in range(n-2):
        n1,n2=n2,n3 #一股Python味儿~
        n3=n2+n1
    print(n3%10007)

def two():
    source=input()
    list1=source.split()
    print(int(list1[0])+int(list1[1]))

#下面的是入门

#杨辉三角

n=int(input())
lastline=[1,1]
nextline=[1]
for i in range(n):
    for j in range(len(lastline)):
        nextline.append(lastline[i-1]+lastline[i])
    