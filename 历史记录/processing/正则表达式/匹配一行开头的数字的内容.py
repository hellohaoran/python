# 作者: 张浩然
# 2022年06月21日20时31分17秒
import re
lin=['15456asd515','4778nijjfk859asdf','asdaf78859','7855542asdfvbg']
for i in lin:
    ret = re.search('\d+',i)
    if ret:
        print('{}匹配成功！'.format(ret.group()))
    else:
        print('{}匹配不成功！'.format(i))