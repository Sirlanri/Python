def xulie(n):
    """
    第一个数是n，后面每一个数都是前一个数整除2,
    """
    lista=[n]
    index=n
    while index>1:
        index=int(index/2)
        lista.append(index)
    print(lista,end=None)

xulie(20)