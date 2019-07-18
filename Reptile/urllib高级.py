import urllib

url = 'http://www.server.com/login'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'  
#values = {'username' : 'cqc',  'password' : 'XXXX' }  
headers = { 'User-Agent' : user_agent }  
request = urllib.request  
response = urllib.urlopen(request)  
page = response.read()   
print(page)

def tou():
    import urllib3
    enable_proxy = True
    proxy_handler = urllib3.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
    null_proxy_handler = urllib2.ProxyHandler({})
    if enable_proxy:
        opener = urllib3.build_opener(proxy_handler)
    else:
        opener = urllib3.build_opener(null_proxy_handler)
    urllib2.install_opener(opener)  