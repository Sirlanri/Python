special = ['x', 'y', 'z']
while 1:
    getnum = input('input')
    if getnum in special:
        after = ord(getnum)-23
    else:
        after = ord(getnum)+3
    print('after:{}'.format(chr(after)))
