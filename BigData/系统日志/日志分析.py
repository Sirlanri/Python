from openpyxl import load_workbook
from pyecharts import options as opts
from pyecharts.charts import Page, Pie
from collections import Counter

alljibie={'信息':0,'错误':0}
result={}
def readexcel():
    allleibie=[]
    file=r'E:\代码\云端同步\保护\多.xlsx'
    wb=load_workbook(file,read_only=True)
    sheet=wb['多']

    jibie=sheet['A1':'A306']
    for cell in jibie:
        if cell[0].value=='信息':
            alljibie['信息']+=1
        if cell[0].value=='错误':
            alljibie['错误']+=1

    leibie=sheet['E2':'E306']
    for cell in leibie:
        allleibie.append(cell[0].value)
    result=dict(Counter(allleibie))
    print(result)
    
def pic()->Pie:
    c=(
        Pie()
        .add('',[list(z) for z in zip(alljibie.keys(),alljibie.values())])
        .set_global_opts(title_opts=opts.TitleOpts(title='警告级别分类'))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    #c.render('级别.html')

def lei() ->Pie:
    so={'常规': 96, '无': 175, '-1': 20, '日志记录/恢复': 12, '-101': 1, '-100': 1}
    c=(
        Pie()
        .add(
            '',
            [list(z) for z in zip(so.keys(),so.values())],
            
            
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="错误类型"),
            
        )
        )
        
    c.render('错误类型.html')


lei()