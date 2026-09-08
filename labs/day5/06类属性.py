# 定义一个 Person 类
class Person:
    # 类属性，保存在类身上
    # 类属性可以通过类访问，也可以通过实例访问
    # 类属性通常用于保存公共数据
    max_age = 120
    planet = '地球'

    # 初始化
    def __init__(self, name, age, gender):
        # 给实例添加属性（语法为：self.属性名 = 值)
        self.name = name 
        self.gender = gender
        if age <= self.max_age:
            self.age = age
        else:
            print(f'年龄超出范围, 已将年龄设置为最大值: {self.max_age}')
            self.age = 120

        

p1 = Person('张三', 18, '男')
p2 = Person('李四', 18, '女')

# 验证一下：实例身上是没有类属性的
# print(p1.__dict__)

# 验证一下：类属性可以通过类访问，也可以通过实例访问
# print(Person.max_age)
# 查找 max_age 的过程：1. p1 -> 2. Person
# print(p1.max_age)

p3 = Person('王五', 133, '男')
p3.planet = '火星'
print(p3.__dict__)
print(Person.__dict__)