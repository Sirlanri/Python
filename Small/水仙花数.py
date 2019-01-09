for x in range (100,1000):
    g=x%10
    s=x//10%10
    b=x//100
    if g**3+s**3+b**3==x:#各位数的三次方
        print(x)
