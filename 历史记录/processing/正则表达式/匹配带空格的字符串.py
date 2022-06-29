# 作者: 张浩然
# 2022年06月21日20时01分10秒
import re
it = ['L smith','k,ing','o,upk','p ls','wnag']
for i in it:
    ret = re.match('\w+(,| )\w$',i)
    if ret:
        print('{}匹配成功！'.format(ret.group()))
    else:
        print('{}匹配不成功！'.format(i))