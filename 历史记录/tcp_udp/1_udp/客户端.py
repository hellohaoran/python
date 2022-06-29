# 作者: 张浩然
# 2022年06月15日10时43分01秒
import socket
import sys
f= open('../The_Holy_Bible.txt','r')
text = []
while True:
    if f.readline():
        text.append(f.readline())
    else:
        break
str_=','.join(text)
print(str_)
str_=str_[0:1900]
f.close()
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)# socket.AF_INET 使用ipv4，socket.SOCK_DGRAM，使用udp协议
dist_addr=(sys.argv[1],2010)



client.sendto(str_.encode('utf8'),dist_addr)
recv_data= client.recvfrom(1052251)
print(recv_data[0].decode('utf8')) # 输出传来的字节流要解码
client.close()
