# 作者: 张浩然
# 2022年06月25日22时06分28秒
class Page:
    def __init__(self,current_page):
        self.current_page=current_page
        self.page_num=10 # 每页的数量是10行
    @property
    def start(self):
        return (self.current_page-1)*self.page_num
    @property
    def end(self):
        return self.current_page*self.page_num
p=Page()
print(p.start)#输出该页最初的行数
print(p.end)#输出该页最后的行数

