#1234四个数字组成的每位都不同的三位数
a=[1,2,3,4]
for g in a:
    for s in a:
        for bai in a:
            if bai!=s and bai!=g and g!=s:
                print(bai*100+s*10+g)