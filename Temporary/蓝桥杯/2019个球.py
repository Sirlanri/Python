
def panduan(num):
    sum=0
    for i in range(1,num+1):
        for j in range(i+1,num+1):
            for x in range(j+1,num+1):
                sum+=1
                
    print(sum)
panduan(2019)