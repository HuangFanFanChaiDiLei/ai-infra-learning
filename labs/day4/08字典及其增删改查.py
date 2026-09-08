# dict - dictionary 字典
# key ---- value
# key 必须是不可变类型
# value 可以是任何类型

# 定义空字典
dict1 = {}
dict1 = dict()

dict1 = {'十面埋伏': '陈奕迅', '稻香': '周杰伦'}
print(dict1)


# 字典可以嵌套
student_dict = {
    20220101: {
        'name': 'Tom', 
        'gender': 'male', 
        'age': 18,

    },
    20220102: {
        'name': 'Alice',
        'gender': 'female', 
        'age': 18},
    20220103: {
        'name': 'Zoom', 
        'gender': 'male', 
        'age': 18}
}
print(student_dict)
list1 = list(student_dict.items())
print(list1)

# 查询 
# 直接取值，若 key 不存在则报错
print(student_dict[20220101]) 
# dict.get()，若 key 不存在，会返回默认值 None，返回值可修改
result = student_dict.get(20220104)
print(result)
result = student_dict.get(20220108, "抱歉，您查找的 key 不存在")
print(result)

# 新增
dict1['传奇'] = '李健'
dict1['暖暖'] = '黄浩男'

print(dict1)

# 遍历
for item in dict1:
    print(item)

# 修改
dict1['暖暖'] = '梁静茹'
print(dict1)
# 批量修改
dict1.update({'传奇': '黄浩男', '暖暖': '美羊羊'})
print(dict1)

# 删除
# del 函数，删除指定键值对
del dict1['传奇']

# dict.pop(key) 删除指定键值对，并返回 key 所对应的 value
result = dict1.pop('暖暖')
print(result)

print(dict1)

# pop 方法可以设置默认值
# 当 key 不存在时会报错，但设置默认值后会返回默认值
result = dict1.pop('四季', "删除失败，您输入的 key 不存在")
print(result)