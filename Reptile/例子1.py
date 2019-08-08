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
    pics=[]
    url='http://tieba.baidu.com/p/6198229867?pn=1'
    web=urllib.request.urlopen(url).read()
    soup=BeautifulSoup(web,features="lxml")
    print(soup.div.string)
    for link in soup.find_all('img'):
        pics.append(link.get('src'))
    
def blog1():
    url='http://liangyj_blog.gitee.io/'
    web=urllib.request.urlopen(url).read()
    soup=BeautifulSoup(web,'lxml')
    titles=soup.find_all('a','post-title-link')
    for title in titles:
        print(title.next)
    
    #after=re.findall('itemprop="url">\S</a>',title)
    
def douban():
        total={}
        users=[]
        url='https://movie.douban.com/subject/24773958/comments?sort=new_score&status=P'
        web=urllib.request.urlopen(url).read()
        soup=BeautifulSoup(web,'lxml')
        comments=soup.find_all('span',class_='short')
        words=soup.find_all('span',class_='comment-info')
        for word in words:
                temp=word.select('a',class_='')
                #users.append(re.findall(r'>\w</a>',temp))
        print(users)

douban()