# 作者: 张浩然
# 2022年06月09日20时41分20秒
import os
import sys


def renam_():
    os.rename('dir/file2','dir/file3')
def remov_():
    os.remove('dir/file3')

def dir_():

    # os.chdir('dir')
    # os.mkdir('dir4')
    # os.rmdir('dir3')
    # print(os.getcwd()) #显示绝对路径
    # print(os.path.isdir('dir/dir1'))
    os.chdir("../")
    dfs('day8',0)
def dfs(path_name,width):
    l = os.listdir(path_name)
    for i in l:
        print(' '*width +i)
        current_path = path_name+'/'+ i
        if os.path.isdir(current_path) :
            dfs(current_path,width+4)
def python_argv():
    '''
    给python传递参数
    :return:
    '''
    print(sys.argv) # sys.argv返回的是列表，argv[0]是他自己的所在文件的绝对路径
    dfs(sys.argv[1],0) #作为参数
def the_holy_bible():
    f = open("The_Holy_Bible.txt",'r+',encoding='utf8')
    f1 = open('The_Holy_Bible2.txt','w+',encoding='utf8')
    while True:
        test=f.readline()
        if test :
            for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
                test = test.replace(ch , ' ')

            test = test.upper()
            f1.write(test)

        else:
            break
    f1.close()
    f.close()
def the_holy_bible2():
    f = open('The_Holy_Bible2.txt','r+',encoding='utf8')
    f1 = open('the_holy_bible2.txt','w+',encoding='utf8')
    count = 0
    word = 0
    dict1 = {}
    while True:
        test = f.readline()
        if test :
            list = test.split(' ')
            dict1 = dict.fromkeys(list,0)
            for i in list:
                dict[i] =
            word += len(list)
            f1.write(list)
            count += 1

def r_():
    f= open('readme','r+',encoding="utf8")
    while True:
        test = f.readline()

        if test:
            test = test.upper()
            f.seek(0,os.SEEK_SET)
            f.write(test)
        else:
            break
    f.close()


if __name__ == '__main__':
    # renam_()
    # remov_()
    # dir_()
    # dfs("dir",0)
    # python_argv()
    # r_()
    the_holy_bible()