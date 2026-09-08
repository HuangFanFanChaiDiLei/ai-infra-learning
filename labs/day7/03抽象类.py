from abc import ABC, abstractmethod

# 【抽象类】是一种不能直接实例化的类
# 它通常作为“规范”，让子类去继承，并实现其中定义的【抽象方法】
# MustRun 类一旦继承了 ABC 类，那么 MUstRun 类就是抽象类了
# ABC = abstract class
class MustRun(ABC):
    @abstractmethod
    def run  (self):
        pass

class Person(MustRun):
    def __init__(self, name, age, gender):
        super().__init__()
        self.name = name
        self.age = age
        self.gender = gender

    def run(self):
        print(f'我叫{self.name}，我在努力的奔跑')

p1 = Person('张三', 18, '男')
p1.run()



class Storage(ABC):  # 继承ABC，变成抽象基类
    @abstractmethod
    def read(self, path):
        pass # 不需要写逻辑，只是契约标记

    @abstractmethod
    def write(self, path, data):
        pass

# 子类
class LocalStorage(Storage):
    def read(self, path):
        print("本地读文件")
    # 故意漏掉 write

# 还没等到调用 write，实例化对象这一行直接抛异常！
# s = LocalStorage()
