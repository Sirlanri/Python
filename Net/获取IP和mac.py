import socket
import uuid

first=socket.gethostname()
ip=socket.gethostbyname(socket.gethostname())#获取本机IP
print(ip)
node=uuid.getnode()
macHex=uuid.UUID(int=node).hex[-12:]
mac=[]
for i in range(len(macHex))[::2]:
    mac.append(macHex[i:i+2])
mac=':'.join(mac)#有点懵逼，mac是怎么出来的？
print(mac)