def one(x:int)->int:
    text=str(x)
    after=''
    textlist=list(text)
    if textlist[0]=='-':
        after=after+'-'
        textlist.pop(0)
    while textlist:
        after=after+textlist.pop()
    return int(after)
print(one(-123))