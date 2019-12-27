special = ['x', 'y', 'z','X','Y','Z']

while 1:
    #输入单个字符串
    getnums = list(input('input'))
    for getnum in getnums:
        if getnum in special:
            after = ord(getnum)-23
        else:
            after = ord(getnum)+3
        print('after:{}'.format(chr(after)))
