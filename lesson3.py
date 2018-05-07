list1=[1,2,3,4,5,6,'a','b']
list2=['A','B']
# list[1]
print(list1[0:-1])
print(list1[1::2])
list1.append(list2)
print(list1)
list1.extend(list2)
print(list1)
del list1[1]
print(list1)

dic={"apple":"苹果","cat":"猫"}
# # dic.popitem()
# dic.values()
# dic.items()
# print(dic)
# dic["apple"]
# dic.get("apple")
dic=dic.fromkeys([1,2,3],"cat")
print(dic)

for i in range(21)

i=1
j=1
for i in range(20):
    i,j=j,j+i
print(i)

小兔子问题
i=1
j=1
count=1
while i<6000:
    i,j=j,j+i
    count+=1
print(i)
print(count)

# tuple=(1,2,3,4,5)
# print(tuple[0::2])

list=[1,2,4,7]
count=0
for i in list:
    for j in list:
        for k in list:
            for l in list:
                if i!=j and i!=k and i!=l and j!=k and j!=l and k!=l:
                    print(i*1000+j*100+k*10+l)
                    count+=1
print(count)

# 以上为复习


list1=[]
for i in range(1,10,2):
    list1.append(i)
print(list1)

def area(a,b):
    # print(a*b/2)
    if a*b/2>0 and a*b/2<=10:
        return "这是一个小三角形"
    elif a*b/2>10:
        return "这是一个大三角形"
    else :
        return "输入值不合法"
print(area(-1,-21))


def tiji(a,b,c):
    print(a*b*c)
tiji(1,2,3)

def judge(a,b):                      #两次print会有none，程序中有print，就可以直接调用函数
    if a*b<0:
        print("error")
    if a*b>0 and a*b<=10:
        print ("little trangle")
    if a*b>10:
        print("big trangle")

print(judge(1,7))

a=[1,2]            # 变量为列表、字典等可以改变的类型时，对变量进行操作，则变量本身会发生改变
def change(a):
    a.append("hello")
    return a
print(change(a))
print(a)

a=10                      # 变量为数字、元组等不可变得类型时，对变量进行操作，只是零时的调用一下该变量，变量本身不发生改变
def change1(a):
    return a*10
print(change1(a))
print(a)

def hello(a):
    return a*"hello"
print(hello(3))

def diedai(*args):           # 星号*表示迭代，对传进去的值自动进行内部迭代
    print(*args)
diedai(1,2,3,4,5,6,7)

def printinfo(a,*b):
    print("输出：")
    print(a)
    for c in b:
        print(c)
    return
printinfo(10)
printinfo(9,8,7,6)

=1，无事，>1，

def fun(i):
    if i==1:
        return 1
    else:
        i+=fun(i-1)
        return i
print(fun(2))

def fun(i):
    if i==1:
        print(i)
    else:
        print(i+=fun(i-1))          # 报错原因：内部迭代正在循环，无法打印出来
fun(2)

def rabbit(a):
    if a==1:
        return 1
    elif a==2:
        return 1
    else:
        sum=rabbit(a-1)+rabbit(a-2)
        return sum
print(rabbit(6))
1 1 2 3 5
def hehua(a):
    if a==1:
        return 1
    else :
        a=hehua(a-1)+hehua(a-1)*2
        return a
print(hehua(3))
1 2 4 8

a=lambda x,y:x^2+y+1
print(a(2,2))

a=10
def fa(a):                    #函数只能看到自己的作用域，即使包含别的函数，但看不见包含的函数的作用域
    a=11
    def fb(a):
        a=12
        return a
    return a 
print(fa(a))

def f1():
    name="a"
    def f2():
        name='b'
        print(name)
    f2()
f1()

name="lzl"                       # 终极版
def f1(): 
    print(name)
def f2():
    name="e"
    print(name)
    f1()
f2()

name="lzl"                       # 打印返回值，为none，class为nonetype
def f1(): 
    print(name)                     
# return ok
print(f1())               # class:nonetype
print(f1)                 # class:function

def outer():
    num=10
    def inner():
        nonlocal num
        num=100
        print(num)
    inner()
    print(num)
outer()

num=1
def f1():
    global num
    print(num)
    num=123
    print(num)
f1()


# li=[lambda x:x for x in range(10) ]      # 打印出的是x对应的内存地址，因为lambda是个函数
# print(li)
# li1=[x for x in range(10)]
# print(li1)
# # 怎么将li打印成li1的形式