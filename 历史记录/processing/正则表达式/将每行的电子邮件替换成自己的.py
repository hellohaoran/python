# 作者: 张浩然
# 2022年06月21日21时39分02秒
import re
l = ['haorankonga@163.com54641523','58645asd485415@163.comasd','58645asd48541asd5@163.comasdlodkkm']

for i in range(len(l)):
    l[i]=re.sub('\w*[\w]{4,20}@(163|qq|162)\.com','3261672092@qq.com',l[i])

print(l)


