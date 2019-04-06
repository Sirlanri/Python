#服务端代码
import socket

words={1:'力量，在我体内流淌！',2:'哦~在这儿停顿！'}
host=''
port=1000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定socket
s.bind((host,port))
#监听一个客户端
s.listen(1)
print('监听端口：{0}'.format(port))
conn,addr=s.accept()
print('连接{}'.format(port))
while 1:
    data=conn.recv(1024)
    data=data.decode()
    if not data:
        break
    print('收到的内容：{}'.format(data))
    conn.sendall(words.get(data,'nothing').encode())
conn.cloes()
s.close()
