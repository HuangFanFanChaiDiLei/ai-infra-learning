class Person:
    max_age = 120
    
    def __init__(self, name, age, id):
        self.name = name    # 公有属性：在 当前类、子类、类外部 中，都可以访问
        self._age = age     # 受保护的属性：在 当前类、子类 中，都可以访问
        self.__id = id      # 私有属性：仅能在 当前类 中访问

    # 注册 age 属性的 getter 方法，当访问 Person 实例的 age 属性时，下面的 age 方法就会被自动调用
    # 加上 property 之后，明明是方法，却不需要()
    @property # property 财产、私人物品
    def age(self):
        return self._age

    # 注册 age 属性的 setter 方法，当修改 Person 实例的 age 属性时，下面的 age 方法就会被自动调用
    @age.setter
    def age(self, value):
        if value <= self.max_age:
            self._age = value
        else:
            print('您输入的年龄非法！')

    @property
    def id(self):
        return self.__id[:6] + '*' * 6 + self.__id[-4:]

    @id.setter
    def id(self, value):
        print('身份证号码不允许修改，如有特殊需求，请联系管理员')


p1 = Person('李华', 22, '410581200312250198')
print(p1.name)
print(p1.age)
p1.age = 99
print(p1.__dict__)
print(p1.id)
p1.id = '111111000000002222'