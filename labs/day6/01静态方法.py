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

    # 静态方法
    # 使用 @staticmethod 装饰过的方法就叫静态方法，静态方法也是保存在类身上的
    # 静态方法只是单纯的定义在类中，不会收到 self、cls 参数，它收到的都是自定义参数
    # 由于静态方法没有收到 self、cls 参数，所以其内部不会访问任何 类和实例的相关内容
    # 静态方法通常用于定义 与类相关的工具方法
    @staticmethod
    def is_adult(year):
        current_year = datetime.now().year
        age = current_year - year
        return age >= 18

    @staticmethod
    def mask_id(id):
        return id[:6:] + '*' * 8 + id[-4::]

# 静态方法需要通过类去调用
result = Person.is_adult(2003)
print(result)
result = Person.mask_id('410581200312250198')
print(result)