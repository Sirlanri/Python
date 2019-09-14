import urllib
from http import cookiejar
import ssl
def qzone(url):
    web=urllib.request.urlopen(url).read()
    #设置忽略SSL验证
    ssl._create_default_https_context = ssl._create_unverified_context

    