# 作者: 张浩然
# 2022年06月21日19时33分47秒
import re
l = ['bat','bit','but','hat','hit','hut']
for i in l:
    ret = re.match('\w{2}t$',i)# {2}t表示t前面有两个字符
    if ret:
        print(ret.group())
    else:
        print('{}不匹配字符串'.format(i))
