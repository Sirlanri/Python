def runNum(start,end):
    """
    计算从起始年份到结束年份的闰年个数
    """
    num=1
    for _ in range(start,end+1):
        num+=1
    return num

def countDay():
    """
    计算有多少天
    """
    runDay=runNum(1921,2020)
    afterDay=365*(2020-1921)
    totalDay=runDay+afterDay
    print(totalDay)
    minutes=totalDay*12*60
    print(minutes)

countDay()