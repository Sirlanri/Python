#输入一年的第几天，转换成月和日
date=int(input('天数多少？'))
mon=[31,28,31,30,31,30,31,31,30,31,30,31]

for y in range(12):
    if date<=mon[y]:
        print(y+1,date)
        break 
    else :
        date=date-mon[y]
