# 定义一个 Person 类
class Person:
    # 初始化
    def __init__(self, name, age, gender):
        # 给实例添加属性（语法为：self.属性名 = 值)
        self.name = name 
        self.age = age
        self.gender = gender

    # 自定义方法
    def speak(self, msg):
        print(f'我叫{self.name}, 年龄是{self.age}, 我想说: {msg}')

class Worker:
    def __init__(self, company):
        self.company = company

    def do_work(self):
        print(f'我在{self.company}工作')

# 定义一个 Student 类，继承自 Person 类
class Student(Person, Worker):
    def __init__(self, name, age, gender, student_id, grade, company):
        Person.__init__(self, name, age, gender)
        Worker.__init__(self, company)
        self.student_id = student_id
        self.grade = grade

    def speak(self, msg):
        print('我是 Student 的 speak 方法', msg)

    def study(self):
        print(f'我是{self.name}, 我正在好好学习, 争取拿到{self.grade}的前 5%')    

s1 = Student('李华', 22, '男', 'SA26225137', '研一', '华为')
print(s1.__dict__)
s1.study() # s1 -> Student -> Person -> Worker -> object
s1.do_work()

# 类的__mro__属性：用于记录属性和方法的查找顺序
# 通过实例去查找 属性/方法 时，先 实例对象，后按照 __mro__ 去寻找
print(Student.__mro__) 