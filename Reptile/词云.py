import urllib
import lxml
import re
from bs4 import BeautifulSoup # 导入网页解析库
import os
from wordcloud import WordCloud #词云
import jieba
import matplotlib.pyplot as plt

#获取网址
allURLs=[]
def getCommit():
    sourceURL='https://movie.douban.com/subject/26581837/comments?start='
    count=0
    while (count<220):
        allURL=str(count).join([sourceURL,'&limit=20&sort=new_score&status=P'])
        count+=20
        allURLs.append(allURL)

#爬虫部分
def getTxt(url):
    pingluns=[]
    web=urllib.request.urlopen(url).read()
    soup=BeautifulSoup(web,'lxml')
    comments=soup.find_all('span',class_='short')
    for comment in comments:
        pingluns.append(comment.string)
    
    #写入TXT文件
    with open('上海堡垒.txt','a',encoding='utf-8')as f:
        for pinglun in pingluns:
            f.write(pinglun+'\n')

#获得完整的txt
def main_txt():
    getCommit()
    for url in allURLs:
        getTxt(url)

#词云
def cloud():
    f=open('上海堡垒.txt','r',encoding='utf-8').read()

    #用jieba包来分词
    wordlist=jieba.cut(f,cut_all=True)
    wl=' '.join(wordlist)

    wc=WordCloud(font_path='msyh.ttc',max_words=700,random_state=30,
    max_font_size=250,width=1920,height=1000)
    myword=wc.generate(wl)#生成词云

    plt.imshow(myword)
    plt.axis('off')
    plt.show()
    #plt.savefig('ciyun3.png')
    #展示词云图

	
cloud()