# 作者: 张浩然
# 2022年06月15日22时07分35秒
import sys
import socket
sever = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)# 传递ipv4，以及用udp协议的socket对象
sever.bind((sys.argv[1],2010)) #监听来自ip地址的 端口号
recv_data = sever.recvfrom(1025)
print(recv_data[0].decode("utf8"))
sever.sendto('i am man it is time to show your manhood'.encode('utf8'),sever.recvfrom(1025)[1])
sever.close()
