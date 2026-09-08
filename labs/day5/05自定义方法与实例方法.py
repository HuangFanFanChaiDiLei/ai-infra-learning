# 定义一个 Person 类
class Person:
    # 初始化
    def __init__(self, name, age, gender):
        # 给实例添加属性（语法为：self.属性名 = 值)
        self.name = name 
        self.age = age
        self.gender = gender

    # 自定义方法是保存在 Person 类身上的，所有 Person 的实例对象都可以调用
    # speak 方法、run 方法，都保存在类身上
    # 但他们主要是供市里调用，所以叫 实例方法
    def speak(self, msg):
        print(f'我叫{self.name}, 年龄是{self.age}, 我想说: {msg}')

    def run(self, distance):
        print(f'{self.name}疯狂的奔跑了{distance}米')

# print(Person.__dict__)

p1 = Person('张三', 18, '男')
p2 = Person('李四', 18, '女')

# 验证：Person 的实例对象上是没有 speak 方法的
print(p1.__dict__)

# 执行 p1.speak() 的时候，查找 speak 方法的过程：
# 1.实例对象自身(p1) -> 2.实例的类(Person)
p1.speak('好好学习')
p2.speak('天天向上')

# 验证：上述查找过程
def speak(msg):
    print(f'我是巴拉巴巴拉，{msg}')
p1.speak = speak
# print(Person.__dict__)
# print(p1.__dict__)
# print(p2.__dict__)
p1.speak('嘿嘿')

# 通过实例去调用实例方法
p1.run(400)

# 通过类去调用实例方法
Person.run(p2, 100)