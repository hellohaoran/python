# 作者: 张浩然
# 2022年06月21日09时16分44秒
import re
ret = re.match('[a-zA-Z0-9_]{8,20}',"1as11f23s343455ff6asdaffggas")# 匹配长度8-20位
print(ret.group())
pres = '85asdxc@163.com'
ret = re.match('[a-zA-Z0-9]{4,20}@163\.com',pres)
print(ret.group())