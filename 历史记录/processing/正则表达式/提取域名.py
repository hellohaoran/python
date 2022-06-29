# 作者: 张浩然
# 2022年06月21日22时34分52秒
import re
l='''http://www.interoem.com/messageinfo.asp?id=35`
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415
'''
l = l.splitlines()
i=0
l1=[]
while i<len(l):
    ret=re.match(r'.*//([^/]+)',l[i])
    l1.append(ret.group(1))
    i+=1
print(l1)

