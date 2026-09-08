dict1 = {'十面埋伏': '陈奕迅', '稻香': '周杰伦'}

# keys 方法：获取 dict 中的所有 key
# 返回值不是 list，而是 dict_keys 
result = dict1.keys()
print(type(result))
print(result)

for item in result:
    print(item)

# 可以借助 list() 函数，将 dict_keys 转变为 list 类型
list1 = list(result)
print(type(list1))
print(list1)

# values 方法：获取 dict 中所有 value
# 返回值不是 list，而是 dict_values
result = dict1.values()
print(type(result))
print(result)

# 可以借助 list() 函数，将 dict_values 转变为 list 类型
list1 = list(result)
print(type(list1))
print(list1)

# items 方法：获取 dict 中所有的键值对（每组键值对以元组形式呈现    
# 返回值是 dict_items 类型
result = dict1.items()
print(type(result))
print(result)