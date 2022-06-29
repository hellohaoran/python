# 作者: 张浩然
# 2022年06月25日23时44分40秒
def m2():
    f=open('file','w',encoding='utf8')
    try:
        f.write('人生苦短，我用python')
    except IOError:# 不能写时
        print('oops')
    finally:
        f.close()
def m1():
     with open('file','r',encoding='utf8') as f:# with open 要起别名
        print(f.read())


if __name__ == '__main__':
    m2()
    m1()