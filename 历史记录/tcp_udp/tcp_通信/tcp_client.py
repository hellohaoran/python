# 作者: 张浩然
# 2022年06月16日21时34分47秒
import socket
import sys

#创建socket套接字对象，SOCK_STREAM是tcp
tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    len(sys.argv) == 2
except:
    print('请输入ip')
    exit(0)
dest_addr=(sys.argv[1],2020)
tcp_client.connect(dest_addr) # 将对象与dest_addr连接
tcp_client.send(b'how are you')#直接调用send发送数据
recv_data=tcp_client.recv(1000)# 接收数据此时recv返回的是数据流
tcp_client.send(b'what are you')# 调用send发送数据
print(recv_data)#打印输出接收到的数据，
tcp_client.close()# 关闭对象