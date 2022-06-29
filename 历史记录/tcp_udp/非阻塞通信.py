# 作者: 张浩然
# 2022年06月17日20时34分11秒
from socket import *
import select
import sys

tcp_server_socket = socket(AF_INET, SOCK_STREAM)

# 别人断线后又重连 可以重用对应地址和端口
tcp_server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# 提醒输入地址
try:
    len(sys.argv)==2
except Exception as e:
    print('请输入ip地址！')
# 本地IP地址和端口

address = (sys.argv[1], 2010)
# 绑定地址与端口
tcp_server_socket.bind(address)
# 激活并监听对方
tcp_server_socket.listen(100)
# 设置tcp_server_socket为非阻塞
tcp_server_socket.setblocking(False)
client_socket = None
# 默认接受时间无限，接受对象无穷
while True:
    try:
        client_socket, clientAddr = tcp_server_socket.accept()
        # 若对方无连接报异常
    except Exception as e:
        # print(e)
        pass
    if client_socket:
        # 设置client_socket为非阻塞
        client_socket.setblocking(False)
        try:
            test = client_socket.recv(1024)
            # 如果对方断开
            if not test:
                print('byebye')
                exit(0)
            print(test.decode('utf-8'))
        except Exception as e:
            print(e)
            pass
