class Dog:
    def speak(self):   
        print("汪汪")

class Cat:
    def speak(self):   
        print("喵喵")

class Pig:
    def speak(self):
        print('哼哼')

# 鸭子多态
def make_sound(animal):     
    animal.speak()   # 同一套调用代码！

dog1 = Dog()
cat1 = Cat()
pig1 = Pig()

make_sound(dog1)
make_sound(cat1)
make_sound(pig1)