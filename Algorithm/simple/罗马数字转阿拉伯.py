def myself():
    luoma = input().lower()
    source = {'i': 1, 'v': 5, 'x': 10, 'l': 50,
              'c': 100, 'd': 500, 'm': 1000, 'z': 0}
    simbles = [item for item in luoma]
    second = []
    poplist = []
    length = len(simbles)
    for i in range(simbles.__len__()):
        if i >= len(simbles)-1:
            break
        if simbles[i]+simbles[i+1] == 'iv':
            second.append(4)
            poplist.append(i)  # 把下标添加到另一个列表里
            i += 1

        elif simbles[i]+simbles[i+1] == 'ix':
            second.append(9)
            poplist.append(i)
            i += 1

        elif simbles[i]+simbles[i+1] == 'xl':
            poplist.append(i)
            second.append(40)
            i += 1

        elif simbles[i]+simbles[i+1] == 'xc':
            poplist.append(i)
            second.append(90)
            i += 1

        elif simbles[i]+simbles[i+1] == 'cd':
            poplist.append(i)
            second.append(400)
            i += 1

        elif simbles[i]+simbles[i+1] == 'cm':
            poplist.append(i)
            second.append(900)
            i += 1

    for index in reversed(poplist):
        simbles.pop(index)
        simbles.pop(index+1)

    for num in simbles:
        second.append(source[num])
    total = 0
    for num in second:
        total += num
    print(total)

def others(s:str):
    count=0
    flag=True
    s=s.lower()
    allnum={'iv':4,'ix':9,'xl':40,'xc':90,'cd':400,'cm':900,'i':1,'v':5,'x':10,'l':50,'c':100,'d':500,'m':1000}
    
    i=0
    while i<len(s):
        if s[i:i+2] in allnum.keys():
            count+=allnum[s[i:i+2]]
            i+=2
        else:
            count+=allnum[s[i]]
            i+=1
    return count
print(others('MCMXCIV'))