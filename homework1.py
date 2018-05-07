# 2018.3.20
list=['A','a','B','b','C','c']
# 取出所有大写字母
print(list[0::2])
# 将所有小写字母顺序倒过来
list.remove('a')
list.remove('c')
list.insert(1,'c')
list.insert(5,'a')
print(list)
# # 想办法生成两个列表，将大小写分开
list1=list[1::2]
list2=list[0::2]
print(list1,list2)

# 2018.3.21
# 利用26个字母创建一个字典A:a
str1='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
str2='abcdefghijklmnopqrstuvwxyz'
for m in str1:
    for n in str2:
        dic={m:n}
print(dic)

# 找出所有值（value）
dic={'A':'a','B':'b','C':'c','D':'d','E':'e'}
print(dic.values())

# # 把字典转化成字符串
# print(str(dic))

# 取出所有的值转化成字典

# 2018.3.22
# 0-100
# 80-100 good
# 60-80 justsoso
# 0-60 bad
# 其他 error

grade=input('请输入成绩：') 
if float(grade)>=0 and float(grade)<=59:
    print('bad!')
elif float(grade)>=60 and float(grade)<=79:
    print("just so so!")
elif float(grade)>=80 and float(grade)<100:
    print("good!")
else:
    print("error!")

# 99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(j,"*",i,'=',i*j,end='\t')
    print(" ")

# 有1,3,5,7四个数字，能组成多少个互不相同且无重复数字的四位数？共多少个？
count=0
for i in range(1,9,2):
    for j in range(1,9,2):
        for k in range(1,9,2):
            for l in range(1,9,2):
                if i!=j and j!=k and k!=l and l!=i and i!=k and j!=l:
                    print(i*1000+j*100+k*10+l)
                    count+=1
print(count)

# 求一个数，它加上100后是一个完全平方数，加上168后还是一个完全平方数
from math import sqrt
x=1
while x>0:
    if sqrt(x+100)-int(sqrt(x+100))==0 and sqrt(x+168)-int(sqrt(x+168))==0:
        print(x)
        break
    x+=1

a=3
b=4
a,b=b,a   #交换值

i=1
j=1
while i<2000:
    i,j=j,j+i
    print(i)