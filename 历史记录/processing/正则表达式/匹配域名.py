# 作者: 张浩然
# 2022年06月21日20时11分09秒
import re
dns=['www.ko.com','www.find.com','www.google.com','www.guilin.edu','www.ksood.net']
for i in dns:
    ret = re.match('www\.\w+\.(com|net|edu)$',i)
    if ret:
        print('{}匹配成功'.format(ret.group()))
    else:
        print('{}匹配不成功！'.format(i))