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
        super().__init__(name, age, gender) # super() 得到父类 Person
        self.student_id = student_id
        self.grade = grade

    # 方法重写：当子类中定义了一个与父类相同的方法，那么子类中的方法就会覆盖父类的方法
    def speak(self, msg):
        print('我是 Student 的 speak 方法', msg)

    def study(self):
        print(f'我是{self.name}, 我正在好好学习, 争取拿到{self.grade}的前 5%')



