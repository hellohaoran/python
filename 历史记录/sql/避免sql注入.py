# 作者: 张浩然
# 2022年06月28日08时31分48秒
from pymysql import *

def main():
    conn=connect(host='192.168.72.133',user='root',password='123',
                 database='python_test',charset='utf8')
    # 获得Cursor对象
    cs1=conn.cursor()
    #构造参数列表 来避免sql注入
    id = ['110000 or 1']
    #执行select 语句，返回值是查出的数据总条数
    count=cs1.execute('select * from areas where aid = %s',id)
    # 打印受影响的行数
    s=cs1.fetchall()
    print(s)
    cs1.close()
    conn.close()
if __name__ == '__main__':
    main()