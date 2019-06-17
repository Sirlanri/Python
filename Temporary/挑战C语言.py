print('摄氏度是{:.2f}'.format(( int(input('华氏度是？'))-32)*5/9))
print('最小值是{}'.format(min([int(n) for n in input().split()])))
print(sorted([int(n) for n in input().split()]))
print(sum (1/i for i in range(1,int(input("算几个数？")))))