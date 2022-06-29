# 作者: 张浩然
# 2022年06月21日20时40分00秒
import re

l='''accept-ch: Sec-CH-UA-Arch, Sec-CH-UA-Bitness, Sec-CH-UA-Full-Version, Sec-CH-UA-Mobile, Sec-CH-UA-Model, Sec-CH-UA-Platform, Sec-CH-UA-Platform-Version
access-control-allow-origin: *
cache-control: public, max-age=432000
content-encoding: br
content-length: 8059
content-md5: LJtDi3F/Bc1gopOE7iDFpA==
content-type: text/javascript; charset=utf-8
cross-origin-resource-policy: cross-origin'''
split_line=l.splitlines()
# print(split_line)
i=0

while i<len(split_line):
    ret = re.search('[a-zA-Z0-9]+',split_line[i])
    print(split_line[i])
    if ret:
        print('{}匹配成功！'.format(ret.group()))
    else:
        print('{}匹配不成功！'.format(split_line[i]))
    i+=1
