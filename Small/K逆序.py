def paixu(list1,k):
    l1=list1[:k]
    l2=list1[k:]
    t1=l1.reverse()
    t2=l2.reverse()

    l=l1+l2
    #l成功生成
    l.reverse()#不能直接print
    print(l)

#正确的简约切片法
def pai(lst,k):
    l=lst[k:]+lst[:k]
    return l

print('正确：',pai([1,2,3,4,5,6,7,8],3))
paixu([1,2,3,4,5,6,7,8],3)

