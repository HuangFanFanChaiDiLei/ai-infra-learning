# 增
# add 添加单个元素
# update 批量添加元素，接收可迭代对象，如：列表、元组、集合

s1 = {1, 2, 3, 4}
s1.add(10)
s1.update([20, 30])
s1.update((11, 22))
s1.update('hello')
s1.update({1, 99})
print(s1)


# 删
# remove 移除指定元素，若元素不存在则报错
# discard 也是移除指定元素，但元素不存在不报错
# pop 从集合中移除一个任意元素，返回移除的那个元素
s1.remove(1)
s1.discard(1)
result = s1.pop()

print(s1)
print(result)

s1.clear()
print(s1)

# 改
# 集合无下标，也不支持 replace 方法，故集合没有专门用于改的方法
# remove + add

set2 = {1, 2, 3, 4}
set2.remove(2)
set2.add(20)

# 查
# 由于集合没有下标，也不支持切片操作，所以集合不具备按位置访问的能力
# 但有成员运算符，通过成员运算符可以判断某个元素是否在集合中

result = 20 in set2
print(result)

result = 20 not in set2
print(result)