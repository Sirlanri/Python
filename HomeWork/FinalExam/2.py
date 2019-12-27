import turtle

def yuan():
    turtle.goto(0, 0)
    turtle.speed(10)
    r = 0.0
    # mmp我竟然自己写出了算法？？？
    # 大体意思就是，每次运动一度，运动完一度，半径+1
    for r, e in zip(range(1, 600, 2), range(0, 360)):
        turtle.circle(r, e)

yuan()