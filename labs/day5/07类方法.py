from datetime import datetime

# 定义一个 Person 类
class Person:
    # 类属性
    max_age = 120
    planet = '地球'

    # 初始化
    def __init__(self, name, age, gender):
        # 给实例添加属性（语法为：self.属性名 = 值)
        self.name = name 
        self.age = age
        self.gender = gender

    # 实例方法
    def speak(self, msg):
        print(f'我叫{self.name}, 年龄是{self.age}, 我想说: {msg}')

    def run(self, distance):
        print(f'{self.name}疯狂的奔跑了{distance}米')

    # 使用 @classmethod 装饰过的方法，就叫类方法
    @classmethod
    def create(cls, info_str):
        name, year, gender = info_str.split('-')
        current_year = datetime.now().year
        age = current_year - int(year)
        # 创建并返回一个 Person 类的实例对象
        return cls(name, age, gender)

    @classmethod
    def change_planet(cls, value):
        cls.planet = value

Person.change_planet('月球')
print(Person.__dict__)

p1 = Person('张三', 18, '男')
p2 = Person.create('李四-2003-女')
print(p1.planet)
print(p2.__dict__)

# 注意：类方法也可以通过实例调用，但是 非常不推荐