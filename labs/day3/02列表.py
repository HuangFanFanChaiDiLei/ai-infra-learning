list1 = list()

list1 = [1, 2, 3, 4]
list2 = list(range(3))

# 增 append、insert、extend
# append() 方法用于在列表末尾添加新的对象。
list1.append(100)
print(list1)

# insert() 方法用于将指定对象插入列表的指定位置。
list1.insert(1, 200)
print(list1)

# extend() 方法用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
list1.extend([300, 400])
print(list1)

list1.extend(list2)
print(list1)

list1.extend('hello')
print(list1)

# 删 pop、remove、clear、del
# pop() 方法用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
result = list1.pop()
print(result)

# pop() 方法也可以指定要移除的元素的索引位置。
result = list1.pop(2)
print(result)
print(list1)

# remove() 方法用于移除列表中某个值的第一个匹配项。
list1.remove(300)
print(list1)

# ValueError: list.remove(x): x not in list
# list1.remove(999) 

# del 语句可以删除列表中的一个元素或多个元素
del list1[0]
print(list1)

del list1[0:2]  # 删除索引为0和1的元素
print(list1)

# clear() 方法用于移除列表中的所有元素。
list1.clear()
print(list1)
