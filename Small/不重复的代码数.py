import os

alllines=[]#所有代码
norepeat=[]#没重复的
filenum=0
codenum=0

def count(path):
    global alllines
    global norepeat
    global filenum
    global codenum

    for filename in os.listdir(path):
        temp=os.path.join(path,filename)#组合路径+文件
        if os.path.isdir(filename):
            count(temp)
        elif temp.endswith('.cpp'):
            filenum+=1
            with open(temp,'r',encoding='UTF-8')as p:
                while 1:
                    line=p.readline()
                    if not line :
                        break
                    elif not line in norepeat:
                        norepeat.append(line)
                        codenum+=1
                p.close()
            print('文件'+filename+'\n不重复行数：'+str(codenum))
            print('文件总数：{0}'.format(filenum))
count('E:\代码\VC') 