
def multiply_table():
    '''
    该函数输出9*9乘法表
    :return:
    '''
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            print("%d*%d=%d"%(i,j,i*j),end = "\t")
            j += 1
        print()
        i += 1