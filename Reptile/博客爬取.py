import os
import re
import ssl
import sys
import urllib

import lxml
from bs4 import BeautifulSoup  # 导入网页解析库


def getDetial(url):
    web = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(web, 'lxml')
    nextbuttons = soup.find_all('a', class_='btn')
    for button in nextbuttons:
        wholeurl = 'https://liangyj_blog.gitee.io'+button.attrs['href']
        artical(wholeurl)


def bigpage():
    source = 'https://liangyj_blog.gitee.io/'
    getDetial(source)
    for i in range(2, 10):
        nextpage = source+'page/'+str(i)
        getDetial(nextpage)


def artical(ori_url):
    url = urllib.parse.quote(ori_url, safe='/:#')
    web = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(web, 'lxml')
    father = soup.find('the')
    if father.string == None:
        father = soup.find('div', class_='post-body')
    sons = father.find_all('p')
    essay = '\n'.join(son.text for son in sons)

    title = soup.find('h1', class_='post-title')
    whole = title.text+'\n\n'+essay+'\n\n'

    print(whole)
    with open('./Reptile/txt/博客.txt', 'a+', encoding='utf-8')as f:
        f.write(whole)


ssl._create_default_https_context = ssl._create_unverified_context
bigpage()
# artical('https://liangyj_blog.gitee.io/2019/08/10/%E7%89%9B%E5%AE%A2%E7%AC%AC%E5%85%AB%E5%9C%BA%E8%A1%A5%E9%A2%98%E5%92%8C%E9%A2%98%E8%A7%A3/#more')
