# 作者: 张浩然
# 2022年06月29日08时17分18秒
def line_6(k,b):
    def create_y(x):
        print(k*x + b)
    return create_y
line_6_1 = line_6(6,2)# 返回create_y（） 的入口地址
line_6_1(4)
line_6_2 = line_6(7,8) # 同样返回create_y()的入口地址
line_6_2(5)
