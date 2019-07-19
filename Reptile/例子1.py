from bs4 import BeautifulSoup
import lxml
import urllib
import re
def mooc():
    http='https://www.icourse163.org/category/computer'
    url=urllib.request.urlopen(http).read()
    print(url.prettify())
    soup=BeautifulSoup(url,features="lxml")
    titles=soup.find_all('.title f-f0')
    print(titles)

def tieba():
    url='http://tieba.baidu.com/p/6198229867?pn=1'
    web=urllib.request.urlopen(url).read()
    soup=BeautifulSoup(web,features="lxml")
    for link in soup.find_all('img'):
        print(link.get('src'))
    
tieba()