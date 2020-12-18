def RmbTodollar(rmb):
    """
    软妹币转美刀
    """
    return rmb*0.1399

def dollarToRmb(dollar):
    """
    美刀转软妹币
    """
    return dollar*7.1477

def tran():
    #主函数
    while 1:
        print('\n选择转换模式\n1 RMB->Dollar\n2 Dollar->RMB')
        flag=int(input())    
        num=int(input('多少钱？'))
        if flag==1:
            print('换算为美元：',RmbTodollar(num))
        else:
            print('换算为软妹币：',dollarToRmb(num))

tran()