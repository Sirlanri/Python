def repeat(a):
    for i in range(2):
        a+=4
        for j in range(5):
            for k in range(6):
                a+=5
            a+=7
        a+=8
    a+=9
    print(a)

repeat(0)