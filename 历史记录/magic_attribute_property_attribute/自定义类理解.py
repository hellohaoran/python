# 作者: 张浩然
# 2022年06月25日23时51分44秒
class File:
    def __init__(self,file_name,open_mode):
        self.file_name=file_name
        self.open_mode=open_mode
    def __enter__(self):
        '''
        enter的返回值给as后的变量名
        :return:
        '''
        self.f=open(self.file_name,self.open_mode,encoding='utf8')
        return self.f
    def __exit__(self, exc_type, exc_val, exc_tb): # 当with语句段结束后自动调用exit的语句
        print('I will exit!')
        self.f.close()
with File('file','r+') as f:
    f.write('坚持练习，就是捷径')