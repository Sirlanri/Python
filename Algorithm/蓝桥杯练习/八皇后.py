#存储合适的八皇后列表，里面是元组
queenList=[]

def isRepeat(x,y):
    """
    判断是否冲突
    """
    global queenList
    if len(queenList)==0:
        return True
    for q in queenList:
        if x==q['x'] or y==q['y'] or x-y==q['x']-q['y']:
            return False
    return True

def findQueen(colume):
    """
    主函数 输入行数列数
    """
    global queenList
    for x in range(colume):
        for y in range(colume):
            if isRepeat(x,y):
                #如果合法，就插入数组
                queenList.append({'x':x,'y':y})
                print(x,y)

findQueen(12)