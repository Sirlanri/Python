def ifsu(num):
    for i in range(2,num):
        if num%i==0:
            return True
    return False

for i in range(10000):
    if not ifsu(i):
        print(i)