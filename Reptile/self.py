import urllib
from urllib.request import Request,urlopen
import requests
from bs4 import BeautifulSoup
import re
import os
import lxml

def getarical(url):
    #web = urllib.request.urlopen(url).read()
    web=requests.get(url,headers={'User-Agent': 'Mozilla/5.0'}).text
    #web=Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup=BeautifulSoup(web,'lxml')
    title_fathers=soup.find_all(class_='post-title')
    index=0
    for title_father in title_fathers:
        if index>2:
            break
        title_link=title_father.contents[1].attrs['href']
        awsl(title_link)
words=[]
def awsl(url):
    web=requests.get(url,headers={'User-Agent': 'Mozilla/5.0'}).text
    soup=BeautifulSoup(web,'lxml')
    wenzis=soup.find_all('p')
    for wenzi in wenzis:
        words.append(wenzi.string)
        print('OK')


def writetofile():
    with open('博客awsl.txt','w+') as txt:
        for word in words:
            if word:
                txt.write(word)
        print('cofirmed')

getarical('https://ri-co.cn/')
writetofile()