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
    