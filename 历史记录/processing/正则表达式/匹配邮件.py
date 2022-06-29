# 作者: 张浩然
# 2022年06月21日10时32分19秒
import re
email_list =['xiaowang@163.comcom','xiaowang@163.com']
for email in email_list:
    ret = re.match('[\w]{4,20}@163\.com$',email)#$前的字符串都是要结尾匹配的，若不匹配,则返回None
    if ret:
        print("%s 是符合规定的邮件地址"%ret.group())
    else:
        print("%s 不是符合规定的邮件地址"%email)