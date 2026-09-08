class Person:
    # 初始化
    def __init__(self, name, age, gender, id):
        self.name = name    # 公有属性：在 当前类、子类、类外部 中，都可以访问
        self._age = age     # 受保护的属性：在 当前类、子类 中，都可以访问
        self.gender = gender
        self.__id = id      # 私有属性：仅能在 当前类 中访问

    def speak(self):
            print(f'我叫: {self.name}, 年龄: {self._age}, 性别: {self.gender}, 身份证号: {self.__id}')

# 此时正常，因为调用的是 Person 的 speak，相当于从 Person 中访问 __id
# class Student(Person):
#     pass

# 正常，可以从 子类 中访问 受保护的属性
# class Student(Person):
#     def speak(self):
#         print(f'我是学生 {self.name}-{self._age}')

# 错误，私有属性进程在 当前类 中访问
# class Student(Person):
#     def speak(self):
#         print(f'我是学生 {self.name}-{self._age}-{self.__id}')

# s1 = Student('李华', 22, '男', '410581200312250198')
# s1.speak()

p1 = Person('李华', 22, '男', '410581200312250198')
print(p1.name)
# 受保护属性，从 类外部 去访问，也能访问到，但是分不推荐！
print(p1._age) 
# 私有属性，从 类外部 不能访问到，而且会报错！
# print(p1.__id)

# python 底层是通过重命名的方式，去实现私有属性的
print(p1.__dict__)  # '_Person__id': '410581200312250198'
print(p1._Person__id)