import re
# str='pythonjavac++phhesf#'
# rules='python'            #最原始的正则表达式
# r=re.compile(rules,re.S);
# match=re.findall(r,str)       #（匹配条件，匹配对象）
# print(match)
# # 或 print(r.findall(str))

# key=r"chuxiuhong@hit.edu.cn"
# p1=r"@.+\."
# p1=r"@.+?\."    # 懒惰模式，匹配到第一个“.”就结束
# pattern1=re.compile(p1)
# print(pattern1.findall(key))

# key=r"wwwwwww192.168.12.1sss333.444.555.666"
# # p1=r"\d+.?\d+.?\d+.?\d+"
# p1=r"(\d+{1,3}\.){3}+\d+{1,3}"
# pattern1=re.compile(p1)
# print(pattern1.findall(key))

# get html text
# <span class="title">换肤</span>
html =  '<span class="top_score">7315</span>'
res=re.findall('<span class="top_score">(.+?)</span>',html)
print(res)
# save

import urllib.request
urllib.request.urlopen