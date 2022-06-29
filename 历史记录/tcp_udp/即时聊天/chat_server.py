# 作者: 张浩然
# 2022年06月17日08时14分02秒
import socket
import select
import sys
tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_addr=('192.168.0.105',2010)
tcp_server.bind(server_addr)
tcp_server.listen(10) # tcp_server对象缓冲的大小
# 如果有新的客户端链接服务器，就产生一个新的套接字专门为这个客户端服务
# client_socket用来为这个客户端服务
# tcp_server可以用来专门等待其他新客户端的链接
client_socket,client_addr = tcp_server.accept()

epoll=select.epoll()
# 告诉epoll监控本机标准输入和为客户端通信的套接字
epoll.register(sys.stdin.fileno(),select.EPOLLIN)
epoll.register(client_socket.fileno(),select.EPOLLIN)

while True:
    events=epoll.poll(-1,2)
    for fd,event in events: # fd 是fileno，envent是事件的类型EPOLLIN
        if fd == sys.stdin.fileno(): # 代表输入缓冲区有数据
            data=input('请输入数据：')
            client_socket.send(data.encode('utf8'))
        elif fd == client_socket.fileno(): # 代表监控到客户端传来数据
            # 接受客户端的数据
            recv_data=client_socket.recv(100)
            if not recv_data:
                print('对方断开！')
                exit()
            print(recv_data.decode('utf8'))
client_socket.close()
tcp_server.close()
