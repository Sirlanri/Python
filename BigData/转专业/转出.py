from openpyxl import load_workbook
from pyecharts.charts import Pie
from pyecharts import options as opts
import re

def test():#测试正则表达式
    #发现自己正则表达式学的太差了，去学会儿正则表达式~
    word='复合材料18-2'
    result=re.search('(\S+)([18])',word)
    result2=re.sub('\d+\-\d','',word)
    print(result2)

