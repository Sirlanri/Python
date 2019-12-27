import os

def one():
    with open('blow_in_the_wind.txt','a+',encoding='utf-8') as f:
        content = f.read()        
        f.seek(0,0)
        f.write('插入头部，歌的名字')
        f.write('歌手的名字')
        f.seek(0,2)
        f.write('1962 by ri-co Inc')

#换个思路
def two():
    second=''
    with open('blow_in_the_wind.txt','r+',encoding='utf-8') as f:
        alllines=f.read()
        first='歌名在头部 '+'随后的歌手名'+alllines
        second=first+'\n1962 by ri-co.cn Inc'
        

    with open('blow_in_the_wind.txt','w+',encoding='utf-8') as f2:
        f2.write(second)
    
    with open('blow_in_the_wind.txt','r+',encoding='utf-8')as f3:
        print(f3.read())
two()#测试成功，注意好文件的位置就行