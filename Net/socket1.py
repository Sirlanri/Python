import socket

#服务器端
def fu():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ip_port=('127.0.0.1',1082)
    s.bind(ip_port)
    s.listen(5) #监听链接请求
    print('已经启动服务端')

    conn,address=s.accept() #等待连接
    while 1:
        client_data=conn.recv(1024).decode()
        if client_data=='exit':
            exit('接收到结束请求，结束通讯')
            break
        print('客户端消息：{}'.format(client_data))
        conn.sendall('回馈消息'.encode())
    conn.close()


#客户端
def ke():
    sk=socket.socket()
    sk.connect('127.0.0.1',9999)

    while 1:
        inp=input('输入要发送的消息').strip()
        if not inp:#防止输入空消息
            continue
        s.sendall(inp.encode())

        if inp=='exit':
            print('客户端结束通讯啦~')
            break

        server_reply=s.recv(1024).decode()
        print(server_reply)
    s.close()
fu()