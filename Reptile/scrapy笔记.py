import scrapy
import random
class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

def choice():
    for i in range(100):
        print('第{}次计算'.format(i))
        a=random.randint(1,9)
        then=(3*a+3)*3
        add=then%10+int(then/10)
        print(add)
choice()