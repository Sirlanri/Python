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


def test2():
    num = 13.6
    int('69.9')
    round()


def test3():
    def nn(x):
        if not isinstance(x, (int, float)):
            print('类型不一样')

        if int(x) > 0:
            return "大于0"
        else:
            return "小于0"

    d = input("输入")
    print(nn(d))


def trim1(s):
    if s[:1] == "":
        s = s[1:]
        if s[-1:] == "":
            return s[:-1]
    else:
        return s


def trim(s):
    if s[:1] == " ":
        s = s[1:]
        if s[-1:] == " ":
            return s[:-1]
        else:
            return s
    elif s[-1:] == " ":
        return s[:-1]
    else:
        return s


def hy1(s):
    while s[:1] == ' ':
        s = s[1:]

    while s[-1:] == ' ':
        s = s[:-1]

    return s
print(hy1(' 58 '))