# 练习 1
fruits = {
    'apple': 4.5,
    'banana': 3.2,
    'orange': 5.8,
    'strawberry': 12.0,
    'honeydew': 8.8
}
# 打印所有水果及其价格
for key in fruits:
    print(f'{key} 价格是 {fruits[key]} 元/斤')

# 找到最贵的水果
# max_price = 0
# max_fruit = str()
# for key in fruits:
#     if max_price >= fruits[key]:
#         continue
#     max_price = fruits[key]
#     max_fruit = key

# key=fruits.get 等号左边的 key：是 max() 函数的形参名
# 它接收一个函数，用来给每个元素计算比较用的分数
# 可以把它理解成：max(序列, 打分函数=xxx)
# 等号右边 fruits.get：字典的 get 方法
# 简而言之，max 里面的 key 是比较函数。只是恰好和 dict 的 key 撞名字了
max_fruit = max(fruits, key=fruits.get)
# def max(iterable, key=None):
#   for element in iterable:  # element就是 fruits的key：'apple'等
#   score = key(element)  # key就是 fruits.get，执行 fruits.get(element)
#   # 根据score比较大小


max_price = fruits[max_fruit]
print(f'最贵的水果是{max_fruit}，价格是{max_price}元/斤')



# 练习 2
students = [
    {
        'name': '张三',
        'scores': {'语文': 88, '数学': 92, '英语': 95}
    },
    {
        'name': '李四',
        'scores': {'语文': 75, '数学': 83, '英语': 80}
    },
    {
        'name': '王五',
        'scores': {'语文': 92, '数学': 95, '英语': 88}
    },
]

# 需求 1: 计算每位同学的平均分
for item in students:
    score_values = item['scores'].values()
    total = sum(score_values)
    average = total / len(score_values)
    print(f'{item['name']}同学的平均分是{average:.2f}')

# 需求 2：找到总分最高的学生
max_scores = 0
max_student = list()
for item in students:
    score_values = item['scores'].values()
    total = sum(score_values)
    if max_scores >= total:
        continue
    max_scores = total

for item in students:
    score_values = item['scores'].values()
    total = sum(score_values)
    if max_scores == total:
        max_student.append(item['name'])

print(f'总分最高的学生是{max_student}，总分是{max_scores}')