#https://www.vmgirls.com

import requests
import urllib.request
from bs4 import BeautifulSoup
import os
import time
import lxml
import re
import ssl

def single(url):
    #此方法已经弃用
    #web=urllib.request.urlopen(url).read()
    with open (url,'rb+') as p:
        web=p
        soup=BeautifulSoup(web,'lxml')
        pic_url=soup.find_all(title="Halcyon")

        for pic in pic_url:
            downpic(pic.attrs['href'])
            

def downpic(url):
    name=url[-12:]
    
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})  # 下载图片，之后保存到文件
    flore=r'E:\代码\妹子\\' + name

    with open(flore,'wb')as f:
        f.write(r.content)
        

def normal_page(url):
    req =urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    web=urllib.request.urlopen(req).read()
    
    soup=BeautifulSoup(web,'lxml')
    imgs=soup.find('div',class_='nc-light-gallery').find_all('img')
    for img in imgs:
        source_url=img.attrs['data-src']
        downpic(source_url)
    print('下载完成')


def bendi():
    #用于测试的
    with open('./Reptile/html/girl4.html','rb+') as web:
        soup=BeautifulSoup(web,'lxml')
        imgs=soup.find('div',class_='nc-light-gallery').find_all('img')
        for img in imgs:
            source_url=img.attrs['data-src']
            downpic(source_url)
        print('下载完成')


def auto(bigurl):
    req =urllib.request.Request(bigurl, headers={'User-Agent': 'Mozilla/5.0'})
    web=urllib.request.urlopen(req).read()
    soup=BeautifulSoup(web,'lxml')
    pic_list=soup.find_all('a',class_='media-content')
    for pic in pic_list:
        normal_page(pic.attrs['href'])


auto('https://www.vmgirls.com/campus')