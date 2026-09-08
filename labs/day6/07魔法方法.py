# 以 __xxx__ 命名的特殊方法
# 不需要我们手动调用，只要准备好这些方法，python 会在特定场景下自动调用
class Person:
    def __init__(self, name, age, gender):
        self.name = name 
        self.age = age
        self.gender = gender

    # 重写 __str__
    # 当调用 print(对象) 或 str(对象) 时会被调用
    def __str__(self):
        return str(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __lt__(self, other):
        return self.age < other.age

    def __getattr__(self, item):
        return f'您访问的 {item} 属性不存在'

p1 = Person('张三', 18, '男')
p2 = Person('李四', 20, '女')

# print(p1)   # python 背后执行的是 p1.__str__
# str1 = str(p1)  # python 背后执行的是 p1.__str__
# print(f'str1 = {str1}')

# __len__ 当调用 len(对象) 时
# res = len(p1)
# print(res)

# __lt__ 当调用 对象1 < 对象2 时
# __gt__ 当调用 对象1 > 对象2 时
# __eq__ 当调用 对象1 == 对象2 时，object 里的 __eq__ 默认比较地址
# print(p1 < p2)

# __getattr__ 当访问不存在的属性时
print(p1.address)