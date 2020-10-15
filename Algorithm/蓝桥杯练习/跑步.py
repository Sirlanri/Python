tili=10000
def run():
    """
    跑步时的函数
    """
    global tili
    tili-=600

def rest():
    global tili
    tili+=300

def exercise():
    global tili
    time=0
    while tili>0:
        run()
        rest()
        time+=2
    tili=tili-300+600
    print(tili,time-2)

exercise()