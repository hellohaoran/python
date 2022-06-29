# 作者: 张浩然
# 2022年06月16日21时34分47秒
import socket
import sys

#创建socket套接字对象，SOCK_STREAM是tcp
tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try :
    len(sys.argv)==2
except Exception as e:
    print('请输入IP地址！')

dest_addr=(sys.argv[1],2010)
tcp_client.connect(dest_addr) # 将对象与dest_addr连接
tcp_client.send(b'how are you')
tcp_client.send(b'wsdafah')


tcp_client.close()# 关闭对象