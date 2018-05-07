# 一：定义一个学生类。有下面的类属性： 
# 1 姓名 
# 2 年龄 
# 3 成绩（语文，数学，英语)[每课成绩的类型为整数] 
# 方法：
# 1 获取学生的姓名：get_name() 返回类型:str 
# 2 获取学生的年龄：get_age() 返回类型:int 
# 3 返回3门科目中最高的分数。get_course() 返回类型:int
class student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def stuname(self):
        return self.name
    def stuage(self):
        return self.age
    def stugrade(self):
        return max(self.grade)
stu=student("hzw",22,[91,92,93])
print(stu.stuname())
print(stu.stuage())
print(stu.stugrade())

# 类里定义的字段是静态字段，调用时用类名直接调用
# 方法里的字段是普通字段

# 普通方法需要传self
# 类方法需要传class
# 静态方法什么都不需要传

# 二：编写一个类，它可以对两个list求交集，并集和差集
# class math:
#     def __init__(self,list1,list2):
#         self.list1=list1
#         self.list2=list2
#     def jiaoji(self):
#         return(self.list1 & self.list2)
# li1=[1,3,5,7,9]
# li2=[3,4,5,6,7]
# re1=math(li1,li2)
# re1.jiaoji()


# 以上为测验
1、property
class Stu:
    def __init__(self, birth=1990):
        self.birth = birth

    @property
    def get_birth(self):
        return self.birth
    
    @property
    def set_birth(self, value):
        self.birth = value

    # birthday = property(set_birth, get_birth)

a = Stu()
a.birthday = 1992
print(a.birthday)

# 2、文件
with open('test.txt','a') as file:
    file.write('hello~')
    print(file.tell())
print(file.closed)
print(file.mode)
print(file.name)

# 创建一个文件夹，文件夹中创建一个文件，并将终端输入内容写到文件中
import os
from subprocess import PIPE,Popen
# os.rename('test.txt','newtest.txt')   #相对路径、绝对路径
# os.system('指令') # 终端
if os.path.exists('C:/hello')==False:
    os.mkdir('C:/hello')
else:
    file=open('C:/hello/test.txt','a')
    # content=os.system('python -V')    #返回值得类型是int
    # file.write(str(content))
    # resp = Popen('python -V',stdout=PIPE)
    resp=Popen('python -V',stdout=PIPE)
    file.write(str(resp.stdout.read()))
    file.close()

import shutil
import glob
import urllib
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode

shutil.copyfile('newtest.txt','newtest2.py')
shutil.move('newtest2.py','test/newtest2.py')
print(glob.glob('*.txt'))

url='https://www.bytelang.com/account/register'
data={'username':'hezuier','password':'shawty0216'}
request_data=urlencode(data)
req=urlopen(url + '?' + request_data)            # get方式
a=req.read().decode()
with open('get方式.txt','a',encoding='utf-8') as file1:
    for i in a:
        file1.write(i)

url='https://www.bytelang.com/account/register'
data={'username':'hezuier','password':'shawty0216'}
data=urlencode(data)
data=data.encode('ascii')            #转换格式
request_data=Request(url,data)             #post方式，封装请求体
with urlopen(request_data) as res:       
    a=res.read().decode()
    with open('post方式.txt','a',encoding='utf-8') as file1:
        for i in a:
            file1.write(i)

import requests
response=requests.get('https://www.baidu.com/')
try:
    with open('request.html','a',encoding='utf-8') as file1:
        for i in response.text:
            file1.write(i)
except:
    print('error')
# print(response.text)

# 3、正则表达式
import re
key = r"2533450@sina.pq.ali.amaz.com"
key1= r"<HtMl><Body><h1>welcome</h1></bODy></hTmL>"
p1 = r"@.+?\."
p2= r"<[^H]+?s>"                     #懒惰/贪婪模式，默认贪婪模式
pattern1 = re.compile(p1)
pattern2 = re.compile(p2)
matcher1 = re.search(pattern1,key)       #search：遇到符合的第一个即结束
print (matcher1.group(0))
print(pattern1.findall(key))   #findall：遍历匹配，返回一个列表
print(pattern2.findall(key1))

