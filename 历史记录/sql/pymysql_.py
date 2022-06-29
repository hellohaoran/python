# 作者: 张浩然
# 2022年06月27日10时40分14秒
from pymysql import *

def main():
    conn=connect(host='192.168.72.133',user='root',password='123',
                 database='jing_dong',charset='utf8')
    #获得cursor对象
    cs1=conn.cursor()
    #执行insert语句
    # count=cs1.execute("insert into goods_cates(cate_name) value('硬盘')")
    # print(count)
    #更新
    # count=cs1.execute("update goods_cates set cate_name ='机械硬盘' where cate_name='硬盘'")
    #删除
    # count=cs1.execute("delete from goods_cates where cate_name= '机械硬盘'");
    #查
    # count = cs1.execute("select  * from goods_cates")
    count = cs1.execute("select  * from goods")

    good=cs1.fetchmany(2)#查询两条数据
    print(good)
    print(count) # 共有多少条数据受影响
    conn.commit()
    cs1.close()
    conn.close()
if __name__ == '__main__':
    main()

