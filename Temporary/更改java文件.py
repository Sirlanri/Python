import os
import os.path
import sys


def listdir(path, list_name):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        elif os.path.splitext(file_path)[1]=='.java':
            list_name.append(file_path)

allfile=[]
def file_name(file_dir): 
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1]=='.java':
                name=os.path.join(root, file)
                allfile.append(name)

def rename():


    for i in range(len(allfile)):
        with open(allfile[i],'w+') as f:
            content=f.read()
            f.seek(0,0)
            temp='package '+secdir[i]+';\n'+content
            f.write(str(temp).encode('utf-8'))


secdir=[]
def lujing():
    for item in allfile:
        
        secdir.append(os.path.split(item[16:-5])[0].replace('\\','.'))#包名
    print(secdir)

onedir=r'E:\代码\云端同步\Java'
test=r'E:\代码\云端同步\Java - 副本\Homework\第三章'
file_name(test)
lujing()
rename()