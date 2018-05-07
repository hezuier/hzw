from selenium import webdriver
browser=webdriver.Chrome(r'C:\Users\HZW\AppData\Local\Google\Chrome\Application\chromedriver.exe')
browser.get('http://www.kugou.com/')
input1=browser.find_element_by_css_selector('[type="text"]').send_keys('女孩')
button1=browser.find_element_by_css_selector('.searh_btn').click()
checkbox1=browser.find_element_by_css_selector('.search_icon.checkall').click()
button2=browser.find_element_by_css_selector('.play_all').click()


if True: 
print ("Answer") 
    print ("True") 
else: 
    print ("Answer") 
    print ("False") # 缩进不一致，会导致运行错误 

a="/.,;[][;...hhhhjdjfeubds....duhcdbsv...djiein.////,,"
a.strip("/.,;[]")
print(a.strip("/.,;[]"))

a="nong"
b="nong"
c="~"
d=a+b+c
print(d)

a="dshfjskbfFJSEHFSKJEF"
print(a.lower())
print(a.upper())
print(a.swapcase())
print(a.capitalize())

print(help(a.strip)) #help文档

from selenium import webdriver
print(help(webdriver)) # 如果有more，可以直接按空格继续查看更多内容

import selenium
print(help(selenium.webdriver))

import pandas as pd
print(help(pd))


i=0
s=0
while i <=1000:
    s=s+i
    i+=1
print(s)

i=0
s=0
while i<=100:
    i+=1
    print("hello")
print(i)


s=0
for i in range(1001)   #i在for后直接被定义
    s=s+i
print(s)

str="hello my name is hanmeimei"
for i in str:          #in后面的代表一个集合
    print(i)

list=["A","B","C","D"]
for i in list:          #in后面的代表一个集合
    print(i)



