list1=list(range(20))
print(list1[::])#输出原列表
print(list1[::-1])#逆向输出
print(list1[::2])#隔一个输出，偶数位置
print(list1[1::2])#隔一个输出，奇数位置
print(list1[3::3])#3的倍数
print(list1[3:11])#输出指定位置之间的

list2=list(range(11))
list2[12:]=[11]#在第12位上插入‘11’
print(list2)
list2[1:5]=[21,22,23,24,25]#替换1-5位
print(list2)
list2[:3]=[]#删除了前三位
print(list2)
list2=list(range(10))
list2[10:]=[11,12,13]#添加到10位之后，也就是增添
print(list2)

#-------总结---------#
#[“起始位置:终止位置:取下一个值的位置于此位置的差]
