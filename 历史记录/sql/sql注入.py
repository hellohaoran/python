# 作者: 张浩然
# 2022年06月28日08时20分55秒
from pymysql import *

def main():
    conn = connect(host='192.168.72.133',user='root',password='123',database='python_test',charset='utf8')
    #获得cursor对象
    cs1 = conn.cursor()
    #sql注入
    id='110000 or 1'# 由于恒真所以会把所有数据读出来
    sql='select * from areas where aid={}'.format(id)
    print(sql)
    #执行sql语句 并查询
    count= cs1.execute(sql)
    print(count)
    #打印受影响的行数
    s=cs1.fetchall()
    print(s)
    cs1.close()
    conn.close()
if __name__ == '__main__':
    main()