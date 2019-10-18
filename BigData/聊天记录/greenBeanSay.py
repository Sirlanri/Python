from openpyxl import load_workbook
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Pie
import re
from collections import Counter

recordpath=r'E:\代码\云端同步\保护\record2.txt'
messages=[]

def openfile(path):#读取文件
    global messages
    with open(recordpath,'r',encoding='utf-8') as f:
        temps=f.readlines()
        while '\n' in temps:
            temps.remove('\n')#删除空格，剩余的元素就是时间/聊天记录
        messages=temps

def whoSpeak():#两人各自的发言数量
    me=her=0
    data={}
    for message in messages:
        if '' in message:#自己名字
            me+=1
        if '' in message:#对方的名字
            her+=1
    print('me{0},her{1}'.format(me,her))
    z=[{"我发送的":me},{"她发送的":her}]
    #可视化
    c=(
        Pie()
        .add('消息',[('我',me),('她',her)])
        .set_global_opts(title_opts=opts.TitleOpts(title='发送消息数量',subtitle='那些年我们追过的女孩'))

    )
    c.render(path='发言.html')

def time():#发言时间,返回一个字典
    times=[]
    all={}
    for message in messages:
        if '2019-' in message or '2018-' in message:
            first=re.search(r'(\d{1,2})\:',message).group()
            after=re.sub(':','',first)
            times.append(after)
    result=dict(Counter(times))
    return result


def test():
    openfile(recordpath)
    whoSpeak()
test()