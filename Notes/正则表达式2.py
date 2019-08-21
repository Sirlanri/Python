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

    final=re.findall('singer="(\w+)">(\w+)<',html1)
    print(final)

def chaifen():
    poem='窗前不止明月光，疑是地上霜；举头看太阳。低头撕裤裆'
    devide=re.split('[,.。;；，]',poem)
    print(devide)

def chongfu():
    infor='张三：0731-8825951，李四：0733-8794561，\
        王五： 985-985634'
    #返回一个列表
    after=re.findall('[\d]{3,4}',infor)
    #返回一个对象...嗯 对象！
    after2=re.search('[\d]{3,4}?',infor).group()
    after3=re.findall('[\d]{7}',infor)

    #试试分组
    after4=re.findall('([\d]{3,4})(-)([\d]{7,8})',infor)#是元组的列表
    fenkai=after4[1][0]
    print(after)

    longnum='''2138675501
        (213)8675502
        213.867.5503
        (213)-867-5504
        1(213)867-5505
        +1-213-867-5506
        '''
    getnumall=re.findall('([\d]{3})[\.]?([\d]{3})',longnum,re.MULTILINE)

def practice1():

    source='''
        张伟 86-14870293148  \n
        王伟   +86-13285654569    \n
        王芳        15856529115    \n
        李伟         13022816340  \n
        王秀英   (86)14785720656     \n
        李秀英    17201444672    \n
        李娜         15682812452     \n
        张秀英         14326967740     \n
        刘伟  15146435743    \n
        张敏        (86)-17712576838   \n
        李静       86 14295083635  \n
        张丽     (+86) 13722348123   \n
        王静         17587918887   \n
        王丽    15493106739    \n
        李强      13786842977   \n
        张静         86-15542304386     \n
        李敏         15642387356 \n
        王敏          18627216756  \n
        王磊       17206185726   \n
        李军      17857426238     \n
        刘洋        17345352790     \n
    '''

    num1=re.findall('[\d]{11}',source)
    num2=re.findall('1[3|8]\d{9}',source)
    num3=re.findall('王\S*',source)
    #错误示范-姓张的手机号
    num4=re.findall('张\S+[\s]+([\d]{11})',source)
    #正确方法
    num5=re.findall(r'(张\S*)\s+\(?(\+?86?)?\)?[ .-]?([\d]{11})',source)

    #格式化电话号
    num6=re.sub(r'[86]*[\+\-\(\)]',' ',source)


    source2='''
        张伟         1996.8.24 
        王伟      1993年10月21日   
        王芳         1997-7-24   
        李伟       1996.3.21  
        王秀英        1991.12.0  
        李秀英     1994-7-5    
        李娜       1999.1.28   
        张秀英        1998-2-24   刘伟     1996.5.28      张敏      1996.10.26   
        李静      1993年1月6日    
        张丽        1992.5.21     王静  1998-5-1  
        王丽   1994-4-14  
        李强  1993.8.13   
        张静          1998年1月5日   李敏    1993-8-21  
        王敏      1997-3-7    
        王磊     1999-3-18    
        李军         1990-12-18  
        刘洋   1995年5月7日  
    '''

    #找到所有时间
    date=re.findall('\d{4}.\d{1,2}.\d{1,2}',source2)
    #1996年之前出生的？？？什么鬼？？
    birth=re.findall('199[0-6].\d{1,2}.\d{1,2}',source2)
    #提取生日
    birthday=re.findall('(\w+).+(\d{4}.\d{1,2}.\d{1,2})',source2)
    after=[]
    after.append(x for x in birthday)
    print(after)
    


practice1()