car={'name':'BMW','price':'100','place':'china'}
print(car)
print(car['name'])#输出对应键位的值
del car['price']#删除价格
print(car)

#长字典
language={
    'tom':'java',
    'joho':'C艹',
    'trump':'python'
}
print('tom最爱的语言是:'+language['tom'].title())# title可以使第一个字母大写
for name in language.keys():#只输出键名
    print(name.title())
for files in language.values():#只输出值
    print(files)

if 'tony' not in language.keys():#判断是否有这个键
    print('这家伙不在')
print(language.values())
#这样输出似乎很正常？上面那个不太正常？喵喵喵？？？
for values in language.values():
    print(values)


#河流的练习
rivers={
    'changjiang':'China',
    'mixixibi':'USA',
    'Amazon':'Baxi',
    'nilo':'Iji'
}
for river in rivers.keys():#输出所有河和国家
    print('河'+river+' 国家'+rivers[river])#我真他喵的是个天才~
#只输出河
for river in rivers.keys():
    print('所有河的名字是{}'.format(river))
#输出国家
for river in rivers.values():
    print('所在的国家是:{}'.format(river))
