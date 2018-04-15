# class Student:                     # 定义类
#     def __init__(self,name,age,id):
#         self.name=name
#         self.age=age
#         self.id=id
#         print("init function must executed before every function")
#     def study(self):                    # 定义函数
#         print('is studying')
#     def coding(self):
#         print('is coding')
#     def asking(self):
#         print('is asking teacher')

# hzw=Student("h",22,041401)    #实例化，创建对象
# # hzw.study("hzw")         # 方法调用
# # hzw.coding()
# # hzw.asking()

# class animal():
#     def eat(self):
#         print("具备吃的能力")
# class human(animal):
#     def love(self):
#         print("具备爱的能力")
# class student(animal,human):
#     def study(self):
#         print("具备学习能力")
# hzw=student()
# hzw.eat()

# 以上为视频学习内容

# 1、面向对象、类、私有类、属性、私有属性
# 声明一个employee类
# class employee:
#     # 类里面的属性
#     pay_raise_amount=1.2
#     __weight=40               # 私有属性,除非在构造器中创建并改变，才会改变其值
#     # 创建一个构造器
#     def __init__(self,first,last,pay,domain="@email.com"):         
#         self.first=first
#         self.last=last
#         self.pay=pay
#         self.email=first+last+domain
    
#     # 创建一个方法
#     def fullname(self):
#         print('{}-{}'.format(self.first,self.last))
#         # return self.first+self.last
    
#     def new_pay1(self):
#         # return self.pay * self.pay_raise_amount
#         return self.pay * employee.pay_raise_amount         # 可能影响到全局

#     def new_pay2(self):
#         return self.pay * self.pay_raise_amount              # 只影响个体
#         # return self.pay * employee.pay_raise_amount

#     def outlook(self):
#         print("{}".format(self.__weight))

#     def __say(self):            #私有方法只有在类的内部被调用
#         print("hello")
#     def isay(self):
#         self.__say()
# # 创建一个类的实例
# emp1=employee("xiaoming","wang",10000)
# emp2=employee("xiaohong","li",10000)
# emp1.outlook()
# emp1.isay()
# # 调用类的一个方法
# # emp1.fullname()
# # # print(emp1.first,emp1.last,emp1.pay,emp1.email)
# # employee.pay_raise_amount=1.5                       # 调用全局，一改都改
# # print("emp1 new pay:",emp1.new_pay1())
# # print("emp2 new pay:",emp2.new_pay2())

# # emp1.pay_raise_amount=1.6
# # emp2.pay_raise_amount=1.6
# # print("emp1 new pay:",emp1.new_pay1())
# # print("emp1 new pay:",emp1.new_pay2())
# # print("emp2 new pay:",emp2.new_pay1())
# # print("emp2 new pay:",emp2.new_pay2())

# emp1.pay_raise_amount=1.7
# emp2.pay_raise_amount=1.7
# print("emp1 new pay:",emp1.new_pay1())
# print("emp1 new pay:",emp1.new_pay2())
# print("emp2 new pay:",emp2.new_pay1())
# print("emp2 new pay:",emp2.new_pay2())
# # print(emp1.new_pay1())

# 2、继承
#类定义
# class people:
#     #定义基本属性
#     name = ''
#     age = 0
#     #定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#     #定义构造方法
#     def __init__(self,n,w,a=10):        # 若想在方法定义的时候赋值，必须将需要赋值的变量放在最后，不然会报错（应该是因为参数太多，最后传参时确定不了哪个是哪个）
#         self.name = n
#         self.age = a
#         self.__weight = w
#     def speak(self):
#         print("%s 说: 我 %d 岁。" %(self.name,self.age))
#     def __siyou(self):
#         print("这是父类私有方法")
#     def sy(self):
#         self.__siyou()
 
# #单继承
# class student(people):
#     grade = ''
#     def __init__(self,n,w,g,a=20):
#         #调用父类的构函
#         # people.__init__(self,n,a,w)
#         super().__init__(n,w,a)                 # super()是可以直接继承父类的一种方法，不需要self
#         self.grade = g
#     #覆写父类的方法
#     def speak(self):
#         print("%s 说: 我在读 %d 年级，我 %d 岁了"%(self.name,self.grade,self.age))

# class speaker():
#     topic = ''
#     name = ''
#     def __init__(self,n,t):
#         self.name = n
#         self.topic = t
#     def speak(self):
#         print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))

# # 多继承
# class sample(student,speaker):
#     a =''
#     def __init__(self,n,a,w,g,t):
#         student.__init__(self,n,a,w,g)
#         speaker.__init__(self,n,t)

# e = sample("xiaoming",10,100,5,"Python")
# e.speak()

# 3、装饰器的作用
class Employee:
    
    name="xiaoming"

    def __init__(self,first,last,pay):
        self.first = first
        self.last  = last
        self.pay = pay

    @property
    def fullname(self):
        return "{} {}".format(self.first,self.last)

    def setName(self,name):
        self.first,self.last = name.split(' ')

    @staticmethod
    def printemail():
        print("email",Employee.name+"@domain.com")

    def __repr__(self):
        return "fullname:{},pay:{}".format(self.fullname,self.pay)

class Manager(Employee):
    employess = []

    def __init__(self,first,last,pay,emp):
        Employee.__init__(self,first,last,pay)
        self.employess = emp

    def delete(self,fullname):
        employess=self.employess
        # 作业：根据姓名删除其中一个成员（用字典的方式）
        # 对今天所学内容做一个思维导图

e1 = Employee('xiao','wang',7000)
e2 = Employee('xiao','hong',8000)
e3 = Employee('xiao','ming',9000)

print(repr(e1))

m = Manager("zhang","san",10000,[e1,e2,e3])
print(m.employess)

# 4、爬虫

