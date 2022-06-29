# 作者: 张浩然
# 2022年06月16日21时46分31秒
import socket
import sys
server_tcp=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 用socket创建服务器对象
dist_local=(sys.argv[1],2020)
server_tcp.bind(dist_local)# 绑定服务器地址与端口
server_tcp.listen(10)# 监听 最大值是10即是10个发送方
client_socket,client_addr = server_tcp.accept()# accept返回一个新的socket对象和对方地址信息 期间进行三次握手
recv_data=client_socket.recv(10) # 从对方收10个字节流的数据
print(recv_data)
recv_data=client_socket.recv(10)# 再从对方收10个字节流的数据，类似列表
print(recv_data)

client_socket.send(b'asasdafaasd') # 发送给对方的数据
recv_data=client_socket.recv(1025)
print(recv_data)
client_socket.close()
server_tcp.close()
