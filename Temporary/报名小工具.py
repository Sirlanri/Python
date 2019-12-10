import os
import re
import lxml
from bs4 import BeautifulSoup 
from openpyxl import load_workbook

money_cs=[]
group=[]
confirmed=[]
drop=[]
def list_excel():
    with open(r'E:\代码\蓝桥杯\all.xlsx','rb+') as biaoge:
        wb=load_workbook(filename=biaoge,read_only=True)
        this_sheet=wb['计院缴费']
        for row in this_sheet['B1':'B181']:
            for cell in row:
                #将计院负责的导入列表
                money_cs.append(cell.value)

def list_html():
    with open(r'E:\代码\蓝桥杯\QQ群2.html','r+',encoding='utf-8') as source_html:
        soup=BeautifulSoup(source_html,'lxml')
        name_blocks=soup.find_all(class_='group-card')
        for name_block in name_blocks:
            text=name_block.string
            whitename=re.sub(r'\s','',text)#获取群内备注
            group.append(whitename)
            
def combine():
    for person in group:
        if person[0:2] in money_cs :
            confirmed.append(person[0:2])
        elif person[0:3] in money_cs:
            confirmed.append(person[0:3])
        else:
            drop.append(person)
            print(person)
    print('\n',len(drop))

def main():
    list_excel()
    list_html()
    combine()

main()