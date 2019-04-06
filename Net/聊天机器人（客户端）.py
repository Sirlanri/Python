import socket
host='127.0.0.1'
port=1000
s=socket.scoket(socket.AF_INET,socket.SCOK_STREAM)
try:
    #连接服务器
    s.connect((host,port))
except Exception as e:
    print('服务器没有打开哟亲亲')
    sys.exit()
while 1:
    c=input('输入消息吧~')
    #发送数据
    s.sendall(c.encode())
    #从服务端接受数据
    data=s.recv(1024)
    data=data.decode()
    print('接收的消息：',data)
    if c.lower()=='bye':
        break
    #关闭连接
    s.cloes()