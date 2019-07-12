import urllib.request

def download(url):#下载网页只需要一句
    return urllib.request.urlopen(url).read()

def download_safe(url):#安全的下载，因为经常出错
    print('开始下载',url)
    try:
        html=urllib.request.urlopen(url).read()
    except() as e :
        print('下载失败咯~',e)
        html=None
    return html

#重复多次下载
def repeat(url,time=2):
    print('下载{0}，次数{1}'.format(url,time))
    try:
        html=urllib.request.urlopen(url).read()
    except(Exception)as e:
        print('下载出错',e)
        html=None
        if time>0:
            return repeat(url,time-1)
    return html

#设置代理
def agent(url,user_agent='wswp',time=2):
    print('使用代理下载',url)
    request=urllib.request.Request(url)
    request.add_header('User-agent',user_agent)
    try:
        html=urllib.request.urlopen().read()
    except() as e:
        print('下载失败啦',e)
        html=None
        if time>0:
            return agent(url,time-1)
    return html

#http代理
def agent_http(url,user_agent='wswp',time=2,charset='utf-8',proxy=None):
    print('使用了http代理 ',url)
    request=urllib.request.Request(url)
    request.add_header('User-gent',user_agent)
    try:
        if proxy:
            proxy_support=urllib.request.ProxyHandler({'http':proxy})
            opener=urllib.request.urlopen(request)
            urllib.request.urlopen(request)
        resp=urllib.request.install_opener(opener)
        cs=resp.header.get_content_charset()
        if not cs:
            cs=charset
        html=resp.read().decode(cs)
    except()as e:
        print('下载出错',e)
        html=None
        if time>0:
            if hasattr(e,'code')and 500<=e.code<600:
                return agent_http(url,time-1)
    return html

#下载限速
from urllib.parse import urlparse
import time
def do_delay():
    delayed=Throttle(delay)#我知道拼写错了，别来提issue
    delayed.wait(url)
    
class Throttle:
    '''添加延时'''
    def __init__(self,delay):
        self.delay=delay
        self.domains={}
    def wait(self,url):
        domain=urlparse(url).netloc
        last_access=self.delay.domains.get(domain)
        if self.delay>0 and last_access is not None:
            sleep_secs=self.delay-(time.time()-last_access)
            if sleep_secs>0:
                time.sleep(sleep_secs)
        self.domains[domain]=time.time()