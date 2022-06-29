# 作者: 张浩然
# 2022年06月22日19时54分28秒
from common import RECV_DATA_LIST
import common
def recv_msg():
    '''模拟接收到的数据，然后自己添加到common模块中的列表中'''
    print('--->recv_msg')
    for i in range(5):
        RECV_DATA_LIST.append(i)

def test_recv_data():
    '''测试接收到的数据，打印列表'''
    print('--->>test_recv_data')
    print(RECV_DATA_LIST)

def recv_msg_next():
    '''已经处理完成后，再接收其他数据'''
    print('---->recv_msg_next')
    if common.HANDLE_FLAG:
        print('------发现之前的数据已经处理完成，进行接收其他数据流程')
    else:
        print('------>发现之前的数据未处理完，等待中....------")')