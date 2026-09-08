# list()、tuple()、set()、dict() 既可以创建空容器，也可以将 【可迭代对象】 转为对应类型
# str() 既可以创建空字符串，也可以将 【任意类型】 转为字符串

list1 = list({'张三': 77, '李四': 88, '王五': 99}) # 默认 .keys()
list2 = list({'张三': 77, '李四': 88, '王五': 99}.values())
list3 = list({'张三': 77, '李四': 88, '王五': 99}.items())
tuple1 = tuple({'张三': 77, '李四': 88, '王五': 99}.items())
set1 = set({'张三': 77, '李四': 88, '王五': 99}.items())
str1 = str({'张三': 77, '李四': 88, '王五': 99})

print(list1, type(list1))
print(list2, type(list2))
print(list3, type(list3))
print(tuple1, type(tuple1))
print(set1, type(set1))
print(str1, type(str1))

dict1 = dict(list3)
dict2 = dict(tuple1)
dict3 = dict(set1)
print(dict1)
print(dict2)
print(dict3)

# 所有的数据容器都支持【成员运算符】 in / not in
print('赵六' in dict1) # 默认 .keys()
print(77 in dict1.values())
print(('张三', 77) in dict1.items())
