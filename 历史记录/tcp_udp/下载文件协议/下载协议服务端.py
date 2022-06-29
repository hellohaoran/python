# 作者: 张浩然
# 2022年06月19日11时02分14秒
''''文件下载协议主要防止粘包'''
import socket
import struct
tcp_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_server.bind(('192.168.0.105',2000))
tcp_server.listen(100)
tcp_server_socket,tcp_Address=tcp_server.accept()
file_name = tcp_server_socket.recv(100)# 返回的是否是元组
tcp_server_socket.send(struct.pack("I",len(file_name)))#第一个参数I代表发送四字节，第二个参数代表发送的长度
tcp_server_socket.send(file_name)#发送文件名
f = open(file_name.decode(),'rb')
f_data=f.read()
tcp_server_socket.send(struct.pack('I',len(f_data)))
tcp_server_socket.send(f_data)#发送文件
f.close()
tcp_server_socket.close()
tcp_server()

