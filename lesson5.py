import re
import requests
import urllib.request as ulib
# 1、爬虫(试试多页的)
response=requests.get('http://www.ivsky.com/tupian/haiyangshijie/index_2.html')
wangzhi=response.text
# file1=open("wangzhi.txt","w+")
# file1.write(wangzhi)
with open("wangzhi.txt",'a',encoding='utf-8') as file1:
    for i in response.text:
        file1.write(i)
pattern=re.compile(r"http://img.ivsky.com/img/tupian/li/.+\.jpg")
res=re.findall(pattern,wangzhi)
print(res)
with open("picture.txt",'a+',encoding='utf-8') as file2:
    for n in res:
        file2.write(n + '\n')
response1=requests.get('http://www.ivsky.com/tupian/haiyangshijie/index_2.html')
wangzhi1=response1.text
pattern2=re.compile(r'(?<=alt=").*?(?=")')
name=re.findall(pattern2,wangzhi1)
print(name)
x=0
for re,x in zip(res,name):              # 若两个列表元素数量一致，则可以直接用Zip，否则可以用ziplonggest，这个需要导入一个包
     ulib.urlretrieve(re,'C:/Users/HZW/Desktop/picture/%s.jpg' % x)


# 2、封装成函数
def geturl(url):
    response=requests.get(url)
    return response.text

def pipei(m,n):
    pattern=re.compile(n,re.S)
    return re.findall(pattern,m)

a=geturl('http://www.ivsky.com/tupian/haiyangshijie/index_2.html')
x=r'http://img.ivsky.com/img/tupian/li/.+\.jpg'
b=pipei(a,x)
print(b)

# 3、豆瓣获取信息（.*? 懒惰匹配的集合）
response3=requests.get('https://movie.douban.com/chart')
douban=response3.text
print(douban)
pattern3=re.compile(r'<div class="pl2">.*?<a href="(.*?)" class>')
db=re.findall(pattern3,douban)
print(db)

# 5、爬虫-多页的
for i in range(1,7):
    if i==1:
        response=requests.get('http://www.ivsky.com/tupian/haiyangshijie/')
    else:
        response=requests.get('http://www.ivsky.com/tupian/haiyangshijie/index_%s.html'%i)
    wangzhi=response.text
    pattern=re.compile(r"http://img.ivsky.com/img/tupian/li/.+\.jpg")
    res=re.findall(pattern,wangzhi)
    with open("wangzhiduoye.txt",'a',encoding='utf-8') as file1:
        for i in response.text:
            file1.write(i)
    print(res)

# 6、程序入口
# if __name__=="__main__":
    
# 7、用python写一个微信自动回复
import itchat
from itchat.content import*
@itchat.msg_register([TEXT])
def reply(msg):
    pattern = re.search('学习',msg['Text']).span()
    if pattern:
        itchat.send("沉迷学习无法自拔",msg["FromUserName"])
    else:
        itchat.send("啦啦啦",msg["FromUserName"])
    
@itchat.msg_register([PICTURE])
def pic_reply(msg):
    itchat.send("666",msg["FromUserName"])

itchat.auto_login()
itchat.run()

# 8、用wordcloud做海报
from wordcloud import WordCloud
import chardet
import matplotlib.pyplot as plt

with open("txt.txt",'r',encoding="utf-8") as file:
    text=file.read()
wc1=WordCloud(background_color="pink",width=1000,height=860,font_path="C:\\Windows\\Fonts\\STFANGSO.ttf",margin=2)
wc2=wc1.generate(text)

plt.imshow(wc2)
plt.axis("off")
plt.show()
wc2.to_file('hzw.jpg')

