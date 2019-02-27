import os
class count(object):
    totalsize=0
    dirnum=0
    filenum=0
    tdir=[]#文件夹目录
    tfile=[]#文件目录
    def __init__(self,path):
        self.check(path)

    def check(self,path):
        if not os.path.isdir(path):
            print('不是文件夹')
        else:
            self.find(path)

    def find(self,path):
        if os.path.isdir(path):
            self.tdir.append(path)
            self.dirnum+=1
            lists=os.listdir(path)
            for list1 in lists:
                self.find(list1)
        else:
            self.tfile.append(path)
            self.filenum+=1
            self.totalsize+=int(os.path.getsize(path))

    def convern(self):
        k,m,g=1024,1024**2,1024**3
        if self.totalsize>g:
            return str(self.totalsize/g)+'G'
        if self.totalsize>m:
            return str(self.totalsize/m)+'M'
        if self.totalsize>k:
            return str(self.totalsize/k)+'K'

    def out(self):
        print('总大小是：',self.totalsize)
        print('文件夹目录：',self.tdir)
        print('文件目录：',self.tfile)
        print('文件夹的数量是：',self.dirnum,'\n文件数量：',self.filenum)

path=count(r'E:\\代码\shadowsocksr-akkariiin-master')