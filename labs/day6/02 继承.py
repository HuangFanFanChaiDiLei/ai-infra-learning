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

    def run(self, distance):
        print(f'{self.name}疯狂的奔跑了{distance}米')


# 定义一个 Student 类，继承自 Person 类
class Student(Person):
    def __init__(self, name, age, gender, student_id, grade):
        # 或者 Person.__init__(self, name, age, gender)  不推荐
        super().__init__(name, age, gender) # super() 得到父类 Person
        self.student_id = student_id
        self.grade = grade

    def speak(self, msg):
        print('我是 Student 的 speak 方法', msg)

    def study(self):
        print(f'我是{self.name}, 我正在好好学习, 争取拿到{self.grade}的前 5%')

# 创建 Student 类的实例对象
s1 = Student('李华', 18, '男', '202215000310', '大一')
print(s1.__dict__)
print(type(s1))

# def speak(msg):
#     print('我是 self 的 speak 方法', msg)
# s1.speak = speak


# 查找 speak、study 方法的过程：1.self -> 2.student 类 -> 3.Person 类
s1.speak('你好')
s1.study()

# isinstance(instance, Class) 判断某个对象是否为知道你各类或其子类的实例
# instance 例子、实例
print(isinstance(s1, Student))
print(isinstance(s1, Person))

# issubclass(Class1, Class2) 判断某个类是否是另一个类的子类
print(issubclass(Student, Person))