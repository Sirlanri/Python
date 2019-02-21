import os
totalsize=0
filenum=0
dirnum=0

def visitdir(path):
    global filenum
    global dirnum
    for lists in os.listdir(path):
        sub_path=os.path.join(path,lists)
        if os.path.isfile(path):
            filenum+=1
            totalsize+=os.path.getsize(sub_path)
        elif os.path.isdir(sub_path):
            dirnum+=1
            visitdir(sub_path)

def main(path):
    if not os.path.isdir(path):
        print('这不是文件夹')
    else:
        visitdir(path)

def convert(size):
    K,M,G=1024,1024**2,1024**3
    if size>=G:
        return str(size/G)+'G'
    elif size>=M:
        return str(size/M)+'M'
    elif size>=K:
        return str(size)+'K'

def output(path):
    print('总大小:',convert(totalsize))
    print('文件夹总数量：',dirnum,'文件数量：',filenum)

path=r'E:\代码\shadowsocksr-akkariiin-master'
main(path)
output(path)