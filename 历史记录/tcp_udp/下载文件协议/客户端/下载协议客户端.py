# 作者: 张浩然
# 2022年06月19日11时25分04秒
import socket
import struct
tcp_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_client.connect(('192.168.0.105',2000))
tcp_client.send('The_Holy_Bible.txt'.encode('utf8'))
file_name_len=tcp_client.recv(4)
file_name=tcp_client.recv(struct.unpack('I',file_name_len)[0])# unpack返回元组，其中第一个元素是file_name
file_len=tcp_client.recv(4)
file=tcp_client.recv(struct.unpack('I',file_len)[0])# 解包返回字节
f=open(file_name,'wb')
f.write(file)
f.close()
tcp_client.close()
