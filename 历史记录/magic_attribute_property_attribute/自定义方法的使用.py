# 作者: 张浩然
# 2022年06月26日09时23分57秒
from contextlib import  contextmanager

@contextmanager
def my_open(path, mode):
    f=open(path,mode,encoding='utf8')
    yield f
    f.close()
with my_open('file','w') as f:
    f.write('心态不要着急要自我肯定')
