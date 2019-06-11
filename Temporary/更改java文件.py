import os
import os.path


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

onedir=r'E:\代码\云端同步\Java'
#file_name(onedir)

def rename():
    for one in allfile:
        with open('one','a') as f:
            f.seek(0,0)
            f.write('package {}'.format())

secdir=[]
def lujing():
    for item in allfile:
        secdir.append(item[15:item.length])#包名
    