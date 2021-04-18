import requests
from lxml import etree

urls = ['http://www.yuedu88.com/yingwuxiong/{}.html'.format(i) for i in range(60963,61065)]

path = './'

def get_text(url):
	r = requests.get(url)
	r.encoding = 'utf-8'
	selector = etree.HTML(r.text)

	title = selector.xpath('//*[@id="BookCon"]/h1/text()')
	
	text = selector.xpath('//*[@id="BookText"]/text()')
	with open(path + title[0], 'w', encoding='utf-8') as f:
		for i in text:
			f.write(i)


for url in urls:
    get_text(url)
