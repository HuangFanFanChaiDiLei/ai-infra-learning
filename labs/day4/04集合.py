# 集合 set, 元素无序，不能通过下标访问，自动去重
s8 = set()
# s = {}  # ❌ 错误，不可定义空 set，此方法定义出来的为 空字典

s1 = {1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 7, 8, 9, 10}
s2 = {'hi', 'hello', '123', 'hello'}
s3 = {10, 'hi', 1, True, 'hi'}

print(s1)
print(s2)
print(s3)

# 可变集合
s2.add('alice')
print(type(s2), s2)

# 不可变集合 frozenset
s4 = frozenset({1, 1, 2, 3, 4})
print(type(s4), s4)

# frozenset 接收的参数可以是任意可迭代对象，但最终返回的一定是不可变集合
s5 = frozenset([1, 2, 3, 4, 4, 4])
s6 = frozenset((20, 30, 30, 30, 40))
s7 = frozenset('hello')

print(s5)
print(s6)
print(s7)

# 集合中不能嵌套可变元素，只能嵌套不可变元素，例如元组 tuple、不可变集合 frozenset
tuple1 = (1, 2)
list1 = [1, 2]
set3 = frozenset({1, 2})
set1 = {11, 22, tuple1}
set2 = {11, 22, set3}
print(set1, set2)