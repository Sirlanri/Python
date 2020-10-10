result=[]
index=0
# 递推
def ditui(n):
    """
    递推1，复杂度指数
    """
    global result,index
    if n <= 2:
        index+=1
        return result[index-1]
    else:
        index+=1
        return ditui(index-1)+ditui(index-2)
        
def feibo(n):
    """
    返回输出数的n-1 + n-2
    """
    global result,index
    if n == 2 or n==1:
        index+=1
        return 1
    elif n==0:
        index+=1
        return 0
    else:
        next=result[n-1]+result[n-2]
        
        index+=1
        return next




def faDitui(n):
    for i in range(n):
        result.append(feibo(i))
    return sum(result)

print(faDitui(100))

