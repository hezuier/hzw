tuplex=(1,2,4,5,6,"hello")  #字符串不可被变更
print(tuplex[5])
a=tuplex[5]
b=a.strip("h")
print(b)
a=b
print(tuplex)

list=['a','s','d','f','K']
i=input()
if i in list:
    print("right")
else:
    print("wrong")

list=[1,4,3,6,8,9,3,5,6,3,0]
list.sort()
print(list)
list1=sorted(list)
print(list1)
print(list*3)

del list
print(list)

dic={"inteilgant":"智能的","AI":"人工智能","youdao":"有道",(""):"苹果7","apple":"苹果x","factory":"富土康"}
dic={ }
dic1=dic.fromkeys(['A','B','C'],['a','b','c'])
print(dic1)
# # dic.popitem()     #随机删除
print(dic[("")])
print(dic)
print(len(dic))
print(str(dic))
# dic.pop("AI")
# print(dic)
del dic["AI"]
print(dic)

tuple=("abc",)           # 定义单个元素，后面要加，否则会自动识别成元素的type
print(type(tuple))