a=[1,2,3] 
if 0:#只要不是0或类似FALSE，都认为是TRUE
    print(a)
else:
    print("noooooooooooooo")
b=[range(10)]
for x in range(10):
    if x:
        print("yes")
    else:
        print("NO")

y=int(input("年龄是？"))
if y>30:
    print("少妇")
elif y<14:
    print("萝莉！")
elif 14<y<18:
    print("未成年的呢...")
else :
    print("是合法的少女！！")
