# 作者: 张浩然
# 2022年06月08日20时00分18秒
def password():
    psw = input("请输入密码！")
    if not psw.isdecimal():
        raise Exception("请输入数字")# 因为不是数字抛出异常
    for i in range(len(psw)):
        if not psw[i] == psw[-(i+1)]:
            raise Exception("请输入正确密码") # 因为 密码不对称抛出异常
    return psw



try:
    print("密码是：{}".format(password()))
except Exception as a:
    print(a)