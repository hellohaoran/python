# 作者: 张浩然
# 2022年06月09日18时38分37秒
import os
def write_():
    f = open('readme','+r',encoding="utf8")
    f.write("人生苦短，我用python\n一切都是对象\n一切都是模块")
    f.seek(0,os.SEEK_SET)
    print(f.read())
    f.close()
def read_line():
    f = open('readme', 'r', encoding="utf8")
    while True:
        text = f.readline()
        if  text:
            print(text,end="")
        else:
            break
    f.close()
def cop_():
    f = open('readme', 'r', encoding="utf8")
    f1 = open('readme1','w',encoding='utf8')
    while True:
        test = f.readline()
        if test :
            f1.write(test)
        else:
            break
    f.close()
    f1.close()
def seek_():
    f = open("readme1",'r+',encoding='utf8')
    f.seek(6,os.SEEK_SET)
    print(f.read())
    f.close()
def a_():
    f = open("readme","a+",encoding="utf8")
    f.write("i will forward")
    f.seek(0,os.SEEK_SET)
    print(f.read())
    f.close() # a+在后面追加 写
def w_plus():
    f = open("readme","w+",encoding="utf8")
    f.write("i love python\nthis is good")
    f.seek(0,os.SEEK_SET)
    print(f.read())
    f.close()# 覆盖写如果原文件有内容，先全部删除然后写既可写又可读
def r_plus():
    f = open("readme","r+",encoding="utf8")
    f.write("how are you\ni am find")
    f.seek(0, os.SEEK_SET)
    print(f.read())
    f.close()# 写的时候，指针在文件开头，并不把原文件内容删除，
def rb_plus():

    f = open("readme","r+",encoding="utf8")
    f1 = open("readme1","rb+")
    f1.write(f.read().encode("utf8"))
    f1.seek(0,os.SEEK_SET)
    print(f1.read())
    f1.close()

    f.close()


if __name__ == '__main__':
    # read_line()
    # cop_()
    # seek_()
    # a_()
    # r_plus()
    rb_plus()