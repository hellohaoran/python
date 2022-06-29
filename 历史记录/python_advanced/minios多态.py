# 作者: 张浩然
# 2022年06月22日20时24分53秒
class MiniOS:
    def __init__(self,name):
        self.name=name
        self.app_list=[]
    def __str__(self):
        if len(self.app_list):
            return '操作系统：{},安装有{}'.format(self.name,self.app_list)
        else:
            return '操作系统：{},安装有{}'.format(self.name,0)
    def os_inst_app(self,app):
        if app.name in self.app_list:
            print('已经安装了 %s,无需再次安装'%app.name)# 操作系统有这个行为
        else:
            app.install()
            self.app_list.append(app.name)
class App:# 软件的父类
    def __init__(self,name,version,desc):
        self.name=name
        self.version=version
        self.desc=desc
    def __str__(self):
        return '%s 的当前版本是%s - %s'% (self.name,self.version,self.desc) # 返回appp版本

    def install(self):
        print('正在将{}[{}]程序安装目录复制到手机上。。。'.format(self.name,self.version))
        print('安装完成！')
class Clion(App):
    pass
class Chrome(App):
    def install(self):
        print('正在解压缩安装程序...')
        super().install()
chrome = Chrome('Chrom','2.0','在windows系统下运行。。')
print(chrome)
clion = Clion('Clion','1.0','在linux系统下运行')
Linux=MiniOS('Linux')
print(Linux)
Linux.os_inst_app(chrome)
print(Linux)
Linux.os_inst_app(clion)
print(Linux)
Linux.os_inst_app(clion)
print(Linux)
