from bs4 import BeautifulSoup
import lxml
import urllib
import re
import os


def mooc():
    http = 'https://www.icourse163.org/category/computer'
    url = urllib.request.urlopen(http).read()
    print(url.prettify())
    soup = BeautifulSoup(url, features="lxml")
    titles = soup.find_all('.title f-f0')
    print(titles)


def tieba():
    pics = []
    url = 'http://tieba.baidu.com/p/6198229867?pn=1'
    web = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(web, features="lxml")
    print(soup.div.string)
    for link in soup.find_all('img'):
        pics.append(link.get('src'))


def blog1():
    url = 'http://liangyj_blog.gitee.io/'
    web = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(web, 'lxml')
    titles = soup.find_all('a', 'post-title-link')
    for title in titles:
        print(title.next)

    # after=re.findall('itemprop="url">\S</a>',title)


def douban():
        # 初始设置好一些东西
    users = []
    pinglun = []
    url = 'https://movie.douban.com/subject/24773958/comments?sort=new_score&status=P'
    web = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(web, 'lxml')

    # 获取评论
    comments = soup.find_all('span', class_='short')
    for comment in comments:
        pinglun.append(comment.string)

    # 获取用户名
    allusers = soup.find_all('span', class_='comment-info')
    for word in allusers:
        users.append(word.select('a', class_='')[0].string)

    # 合并成一个字典
    result = dict(zip(users, pinglun))
    for key in result.keys():
        print(key, '\n', result[key], '\n\n')

    # 写入文件
    with open('豆瓣爬虫_复联三.txt', 'a', encoding='utf-8') as f:
        for key in result.keys():
            words = ''.join([key, '\n', result[key], '\n\n'])
            f.write(words)


douban()
