# 作者: 张浩然
# 2022年06月28日08时46分17秒
from pymysql import connect
def main():
    #创建connection连接
    conn = connect(host='192.168.72.133', port=3306,
                   database='python_test', user='root',
                   password='123', charset='utf8')
    # 获得cursor指针对象
    cs1=conn.cursor()
    #插入10条数据
    for i in range(100000):
        s= cs1.execute("insert into students value (0,'张浩然',18,165,1,'0',1,'1996-3-13')")
    conn.commit()
if __name__ == '__main__':
    main()

