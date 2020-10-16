#假定100个人，只有一个感染者
costDic={}

def getCost(knum):
    """
    传入K值，计算用掉的数量
    """
    global costDic
    if 100%knum!=0:
        return
    firstUse = int(100/knum)
    total=firstUse+knum
    costDic[total]=knum


def bigFind():
    """
    循环控制K的函数
    """
    global costDic
    for num in range(1,51):
        getCost(num)
    
    #排序
    after=sorted(costDic.keys())
    print(after)

bigFind()