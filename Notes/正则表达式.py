import re
t='i wanna something just like this'
x=re.match('wan',t)#从头位置匹配i，如果没有，就返回none
print(x)

y=re.search("wan",t)#扫描整个字符串
y1=re.search('wan',t).span()#返回位置
print(y,y1)

t1=re.sub('this','fuck',t)#把this替换成fuck
t2=re.sub('th','oo',t,1)#替换1次
print(t1,t2)

text='alpha.beat...gamma delet'
x=re.split('[\. ]+',text)
x=re.split('[\, ]',text,maxsplit=1)#最多分割一次
x=re.split('\b',text)
x=re.findall('[a-zA-Z]+',text)
x=re.sub('alpha','google',text)#被替换的旧词，新替换词
x=re.sub('al|be|ga|de','google',text)#只要有其中一个，就替换
print(x)

#删除多余的空格
te='aaa    bb    c d e    fff   '
s=' '.join(te.split( ))#一步到位
s=re.split('[\s]+',te)
s=' '.join(s)
s=re.sub('\s+',' ',te)#把多个空格替换成一个空格
print(s)

exm='shandong university of technology have a lot goodlooking girls'
s=re.findall('\\bg.+?\\b',exm)#字母g开头的单词，？表示非贪心模式
s=re.findall('\\ba.+\\b',exm)#贪心模式，一直输出到最后
s=re.findall('\\ba\w*\\b',exm)
s=re.findall('\\Bo.+?\\b',exm)#开头不是o但是中间有o
s=re.findall('\\b\w.+?\\b',exm)#所有的单词
s=re.findall('\\w+',exm)#也是所有的单词
s=re.findall(r'\b\w.+?\b',exm)#原始字符串
print(s)

#正则表达式对象
ex='shandong university of technology have a lot goodlooking girls'
pat=re.compile(r'\bu\w+\b')#查找u开头的单词
pat=re.compile(r'\b\w+g\b')#g结尾
pat=re.compile(r'\b\w{3}\b')#长度是3的单词
s=pat.findall(ex)
t=pat.search(ex).span()#在ex中搜索pat内容

pat=re.compile(r'\b\w*a\w*\b')
t=pat.findall(ex)
t=re.findall(r'\b\w*y',ex)
print(t)
pat=re.compile(r'\b\w*g\w*\b')
t=pat.findall(ex)
t2=pat.sub('*',ex,1)#只把有g的单词替换一次
pat=re.compile(r'g')
t2=pat.split(ex)
print(t2)
print("------------")

#match
email='tony@tiremove_thisger.net'
m=re.findall('remove_this',email)#在email中寻找字符
m=re.sub('remove_this','',email)#直接sub替换
m=email.replace('remove_this','')#使用replce替换

m=re.match(r'(\w+) (\w+)','that girl, boy next door')
print(m.group(0))#返回全部内容
print(m.group(1))#返回内容的第一部分
print(m.group(2))#返回内容的第二部分
print(m.group(1,2))#返回第一和第二部分


#子模式拓展语法
m=re.match(r'(?P<first_name>\w+) (?P<last_name>\w+)','Zhang Tianyu')#为子模式命名
print(m.group('first_name'))
print(m.group('last_name'))
print(m.groupdict())#以字典形式输出
m=re.match(r'(\d+)\.(\d+)','3.1415')
print(m.groups())#返回所有结果
print(m.group(1))#返回第一部分
print('\n\n\n')

#提取电话号

telword='this is my number:999-2331546 and 233-985671'
pattern=re.compile(r'(\d{3,4})-(\d{7,8})')
index=0
while 1:
    result=pattern.search(telword)#从上次停下的位置继续下次搜索
    if not result:
        break
    print('---------------')
    for i in range(3):
        print('号码：',result.group(i))#分别输出号码的不同部分
        print('开始 ',result.start(i),' 结束 ',result.end(i))#分别起始和结束的位置
        print('位置 ',result.span(i))#起始&结束
    index=result.end()
