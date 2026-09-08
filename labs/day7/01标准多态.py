# 多态
# 同一个接口，传入不同对象，自动执行各自版本的逻辑。
# 重点：调用方不需要关心你到底是什么子类，统一调用同一个方法名。

class Animal:
    def speak(self):
        print('动物正在叫')

class Dog(Animal):
    def speak(self):   # ✅ 重写
        print("汪汪")

class Cat(Animal):
    def speak(self):   # ✅ 重写
        print("喵喵")

# 标准多态
def make_sound(animal: Animal):     # 类型注解：必须传入 Animal 类及其子类
    animal.speak()   # 同一套调用代码！

animal1 = Animal()
dog1 = Dog()
cat1 = Cat()

make_sound(animal1)
make_sound(dog1)
make_sound(cat1)
