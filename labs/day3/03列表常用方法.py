# index，查找指定元素在列表中第一次出现的下标，返回值：下标
list1 = [1, 2, 3, 4, 5]
print(list1.index(3))  # 输出: 2
print(list1.index(3, 1, 4))  # 输出: 2 (在索引1到4之间查找)
# ValueError: 5 is not in list
# print(list1.index(5, 0, 3))  # 错误 (在索引0到3之间查找)


# count，统计指定元素在列表中出现的次数，返回值：次数
list2 = [1, 2, 3, 4, 5, 3, 2, 1, 3]
print(list2.count(3))  # 输出: 3
print(list2.count(6))  # 输出: 0 (元素6不在列表中)


# reverse，反转列表中的元素，返回值：None
list2.reverse()
print(list2)  


# sort，排序列表中的元素，返回值：None
list2.sort()  # 升序排序
print(list2)  
list2.sort(reverse=True)  # 降序排序
print(list2)