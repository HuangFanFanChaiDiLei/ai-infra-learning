# 定义一个 Person 类
class Person:
    # 说明：当一个函数被定义在了类中时，那么这个函数就被称为 方法
    # __init__方法：初始化，给当前正在创建的实例对象添加属性
    # __init__方法收到的参数：当前正在穿件的实例对象（self）、其他的自定义属性
    # 当我们以后编写代码去创建 Person 类实例的时候，python 会自动调用 __init__
    def __init__(self, name, age, gender):
        # 给实例添加属性（语法为：self.属性名 = 值)
        self.name = name 
        self.age = age
        self.gender = gender

# 创建 Person 类的实例对象
p1 = Person('张三', 18, '男')
p2 = Person('李四', 18, '女')

# 直接打印，会输出 <__main__.Person object at 内存地址>
# print(p1)

# print(p1.name)
# print(p1.age)
# print(p1.gender)

# 通过 实例.__dict__ 可以查看所有属性
print(p1.__dict__)
p1.name = '阿三'
print(p1.__dict__)

# 实例可以追加属性
p1.address = '河南安阳'
print(p1.__dict__)