# 查询网站的信息
from urllib import robotparser
import whois


def chaxun():
    print(whois.whois('google.com'))


def robots(url):
    a = {}
    rp = robotparser.RobotFileParser()
    rp.set_url(url)
    a['网址'] = rp.read()
    a['好爬虫'] = rp.can_fetch('GoodCrawler', url)
    a['恶意爬虫'] = rp.can_fetch('Bad', url)
    a['Google'] = rp.can_fetch('Googlebot', url)
    print(a)


robots('https://www.taobao.com/robots.txt')
