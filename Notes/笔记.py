print(44496,end=" ")#数字可以不加引号
print("测试")#输出文字要加引号
print('不分行',end="")#不分行
print(r"输出原字符\n\n")#用r保持原字符不变
#text=input('输入一个字符')#提示并输入一个字符


a, b, c, d = 20, 5.5, "inter", 4+3#同时定义多种不同的数据
print(type(a),type(b),type(c),type(d))#可以输出类型

x=19%3#求余数
print (x)

list1 = ['bcc',123,45.6]#列表
list2=['text',99/9]
print(list1+list2)#同时合并输出两个列表

a=[1,2,3,4,5,6,7,8,9]#输入一个数组（list）
a.pop(3)#删除第三位
a.insert(3,4)#插入到第三位
print (a[0])#输出数组的第一个数值
print(a[2:])#输出数组从第三个数开始到最后一个数
print(a[2:6])#输出第三到第七个数
a[1:3]=[9,8,7]#更改数组的2-4位
print (a)#输出数组
len(a)#输出list中的元素个数

#a,append(10)#将10添加到数组末尾
#a,insert (1,11)#将11插入到1号位上

c=[1,2,3,11,12]
print(a+c)#合成一个数组输出

e={'001','002','003'}#集合用大括号表示，中间需要引号

g1={('第一项'),('second')}#创建一个字典g，有无括号均可
g2={'2第一','2第二'}
print(g1,g2)
f={}#定义f为空字典，字典靠固定的键位定位
f[1]="第一"#对相应键位输入
f[2]="第二"
print (f[1])     # 输出键为 '1' 的值
print (f[2])           # 输出键为 2 的值
print (f)          # 输出完整的字典
print (f.keys())   # 输出所有键
print (f.values()) # 输出所有值

h=[1,2,3,4,5]
print(h[::-1])#反向输出数组
print(h[::-1][:3])#反向输出前3个数

a!=b#表示a不等于b
h=1
i=2
if (h==i):#简单的if判断语句
    print("正确！")
else:
    print("不对！")
x=h!=i#正确
y=h==i#错误
print(x and y)#判断的，数学知识_(:з」∠)_
print(y or x)#一个对就算对
print(not(y and x))#否定你懂得~

print("\n\n\n---------------\n")
k=0#利用for循环计算
j=[1,2,3,4,5]
for num in j:
    print(num)
    k=k+num
print(k)

