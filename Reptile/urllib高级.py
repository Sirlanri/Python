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
