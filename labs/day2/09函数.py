def order(dish, number, pre_price):
    print(f'点了{number}份{dish}，单价{pre_price}元/份，总价是{number * pre_price}元')

# # 位置参数，必须按顺序传入
# order('宫保鸡丁', 2, 20)
# # 关键字参数，可以换位置
# order(number=1, dish='鱼香肉丝', pre_price=15)
# # 混用，位置参数必须在关键字参数前面
# order('麻婆豆腐', pre_price=18, number=3)

# # 限制传参方式, / 前面只能用位置参数， * 后面只能用关键字参数
# def greet(name, /, gender, age, *, height, weight):
#     print(f'姓名：{name}，性别：{gender}，年龄：{age}岁，身高：{height}米，体重：{weight}公斤') 

# greet('小明', '男', 18, height=1.75, weight=65)

# 参数默认值，默认参数必须放在可选参数的后面
def greet2(name, gender='男', age=18, height=1.75, weight=65):
    print(f'姓名：{name}，性别：{gender}，年龄：{age}岁，身高：{height}米，体重：{weight}公斤') 

greet2('小红')