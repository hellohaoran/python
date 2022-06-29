# 作者: 张浩然
# 2022年06月16日22时46分56秒
import socket
import select# epoll在select包中
import sys
tcp_client =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
dest_addr=('192.168.72.133',2010)
tcp_client.connect(dest_addr)# 链接服务器

epoll=select.epoll() #导入epoll

#告诉epoll监控标准输入以及tcp_client的行为,EPOLLIN是读事件类型，epoll.register(文件编号,事件类型)
epoll.register(sys.stdin.fileno(),select.EPOLLIN)
epoll.register(tcp_client.fileno(),select.EPOLLIN)
while True:
    events=epoll.poll(-1,2) # poll第二个参数是等待事件最大数，第一个参数-1表示无限期等待
    for fd,event in events:
        if fd == sys.stdin.fileno(): # 代表本机标准输入里有数据
            data=input("请输入数据：")
            tcp_client.send(data.encode('utf8'))
        elif fd == tcp_client.fileno(): # 去看对方有无发来数据
            recv_data=tcp_client.recv(100)
            if not recv_data:
                print('对方断开了')
                exit()
            print(recv_data.decode('utf8'))

tcp_client.close()
