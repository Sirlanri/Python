import re


def shuzi1():
    #re.match从开头开始匹配
    result=[]
    content = 'Hello 1234567 is a number. 999 Regex String'
    #从头开始匹配hello+数字 match只能从头匹配
    result.append(re.match('^Hello \d',content))
    #匹配第一个数字
    result.append(re.search('\d',content))
    #匹配连续的数字,但是只匹配一段连续的
    result.append(re.search('\d+',content))
    #匹配全部的,findall会返回一个列表
    result2=re.findall('\d+',content)

    
    #输出匹配到的内容
    for i in result:
        print(i.group(0))#返回的是一个match对象
    print(result2)

def wangye():
    '''利用正则表达式查找歌手和歌名'''

    html1 = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
        </ul>
    </div>'''

    final=re.findall(r'singer="(\s+)"',html1)
    print(final)

shuzi1()
wangye()