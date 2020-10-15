#存储合适的八皇后列表，里面是元组
queenList=[]
count=0
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

def findQueen(firstX,fitstY):
    """
    输入第一个行数列数
    """
    global queenList,count
    for x in range(firstX,8):
        for y in range(fitstY,8):
            if isRepeat(x,y):
                #如果合法，就插入数组
                queenList.append({'x':x,'y':y})
                print(x,y)
                count+=1
                break
    queenList=[]
    print()
    

def firstQueen():
    """
    生成第一个皇后的位置
    """
    for x in range(8):
        for y in range(8):
            findQueen(x,y)

firstQueen()
print(count)