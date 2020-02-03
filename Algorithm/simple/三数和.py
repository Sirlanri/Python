def one(nums:[int]):
    nums=sorted(nums)
    confirmed=[]
    length=len(nums)

    x=0
    y=length-1
    middle=int(length/2)
    flag=True

    while x <= int(length/2):
        one=nums[x]
        while y>middle:
            if not flag:
                flag=True
                break
            two=nums[y]
            third=-one-two

            if third>=0:
                for z in range(int(length/2),length):
                    if nums[z]==third:
                        confirmed.append([one,two,third])
                        nums.pop(y)
                        nums.pop(z)
                        nums.pop(x)
                        length-=3
                        y-=3
                        x+=2
                        flag=False
            else:
                for z in range(int(length/2),x,-1):
                    if z==third:
                        confirmed.append([one,two,third])
                        nums.pop(y)
                        nums.pop(z)
                        nums.pop(x)
                        length-=3
                        y-=3
                        x+=2
                        flag=False
            y-=1
        x+=1
    return confirmed
print(one([-1, 0, 1, 2, -1, -4]))