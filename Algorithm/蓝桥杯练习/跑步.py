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
        time+=1
    print(tili,time)

exercise()