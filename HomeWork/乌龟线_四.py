import turtle

#正方形框框的函数
def fangxing():
    turtle.pencolor("black")
    turtle.goto(0,0)
    turtle.speed(9)
    for i in range(100,900,30):
        turtle.forward(i)
        turtle.right(90)
    input()#用于暂停


#圆圆圆的函数
def yuan():
    turtle.goto(0,0)
    turtle.speed(20)
    r=0.0
    #mmp我竟然自己写出了算法？？？
    #大体意思就是，每次运动一度，运动完一度，半径+1
    for r,e in zip(range(1,600,2),range(0,360)):
        turtle.circle(r,e)
    input()


#田字格
#试图用一种算法来输出
def tian():
    for i in range(1,12):
        if(i==1 or i==6 or i==11):
            print('+ - - - - + - - - - +')
        else:
            print('|         |         |')

#写函数名来调用相关函数          
yuan()