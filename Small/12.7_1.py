#删除数列中的数字

a=list(input('输入数字和字母'))
i=0
for y in a:
        if y in range (10):
                del a[i]
        i=i+1
print (a)
