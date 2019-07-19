from bs4 import BeautifulSoup
import lxml
import re
#一个演示用的html
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""  

soup=BeautifulSoup(html)
print(soup.prettify(),'完整输出\n\n\n')
print(soup.title)
print(soup.a)#只查找第一个标签，后面的不做查找
#获取标签内的文字内容
print(soup.b.string)
#P标签的所有属性，得到一个字典
print(soup.p.attrs)
#输出标签属性字典其中的name属性
print('name属性是 ',soup.p.attrs['name'])

#将直接子节点以列表的形式输出
print(soup.a.contents)
#chridren不是列表，要用for输出
for child in soup.a.children:
    print(child)

#子孙节点
for child in soup.p.descendants:
    print('子孙节点',child)

#父节点
p=soup.p
print(p.parent.name)

#查找所有的标签
print(soup.find_all('a'))
#使用正则表达式查找
print(soup.find_all(re.compile('^p')))

#CSS选择器
print('\n\nCSS')
print('标签名',soup.select('title'))#通过标签名
print('class名',soup.select('.sister'))#通过类名
print('ID搜索',soup.select('#link3'))#通过ID搜索

