# 这他喵的是数学题啊！！！
sumnum = 0


def fuckoff(num=10):
    global sumnum
    if num == 0:
        sumnum = sumnum+1
    elif num > 0:
        one = num
        fuckoff(one-1)
        fuckoff(one-2)
        fuckoff(one-3)


fuckoff()
print(sumnum)
