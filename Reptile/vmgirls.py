#https://www.vmgirls.com/3706.html

import requests
import urllib.request
from bs4 import BeautifulSoup
import os
import time
import lxml
import re

def single(url):
    #web=urllib.request.urlopen(url).read()
    with open (url,'rb+') as p:
        web=p
        soup=BeautifulSoup(web,'lxml')
        pic_url=soup.find_all(title="Halcyon")

        for pic in pic_url:
            downpic(pic.attrs['href'])
            

def downpic(url):
    
    name=re.findall('\d\d\-\d\d\-\d\d\.jpg',url)[0]
    flore='./妹子/'.join(name)
    with open(flore,'wb')as file:
        file.write()
    
single('girl.html')