import os
import re
import lxml
from bs4 import BeautifulSoup  # 导入网页解析库
import requests

suoyou=[]

def writein():
    global suoyou
    with open('./Reptile/txt/自己博客.txt', 'w+', encoding='utf-8')as f:
        for one in suoyou:
            for pra in one:

                f.write(pra)
            print('写入完成{}'.format(one[1]))

def getdetail(posturl): #每个post的全部内容
    global suoyou
    quanwen=[]
    r = requests.get(posturl, proxies={"https": "http://127.0.0.1:1080"}).text
    soup2=BeautifulSoup(r,'lxml') 
    title=soup2.find('h2').text
    quanwen.append('-------------'+'\n')
    quanwen.append(title)
    zhengwen=soup2.find_all('p')[0:-2]
    for zheng in zhengwen:
        quanwen.append(zheng.text+'\n')
    quanwen.append('\n\n\n')
    suoyou.append(quanwen)
    print('添加完毕:{}'.format(title))


def getallposts(source):
    r = requests.get(source, proxies={"https": "http://127.0.0.1:1080"}).text
    soup = BeautifulSoup(r, 'lxml')
    posts=soup.find_all(class_='readmore')
    postslist=[]
    for post in posts:
        postslist.append(post.contents[1].get('href'))
    
    for post in postslist:
        getdetail(post) #调用获取文章详情

def main():
    urls=['https://ri-co.cn/','https://ri-co.cn/page/2/','https://ri-co.cn/page/3/','https://ri-co.cn/page/4/']
    for url in urls:
        getallposts(url)
    print('爬取完毕，开始写入')
    writein()
main()