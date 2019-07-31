def god():
    per = 1.0
    for i in range(int(input())):
        num = int(input())
        for j in range(0, num):
            per *= float(num-j)/float(num)
    print('{}%'.format(round(per*100, 3)))


def xinlang():
    import math
    for i in range(int(input())):
        all, wrong = map(int, input().split())
        n = math.factorial(wrong)
        print(n)

def zhuan():
    after = {}
    time = 1
    while 1:
        input()
        source = [(input().split(' '))]
        if 0 in source and len(source) == 1:
            break
        minnum = min(source)
        move_num = 0
        for i in source:
            if i > minnum:
                move_num += i-minnum
                time += 1
        after[time] = move_num
    for key in after.keys:
        print('Set #{}\nThe minimum number of moves is{}'.format(
            key, after[key]))