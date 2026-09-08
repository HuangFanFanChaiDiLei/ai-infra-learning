# A.difference(B) 找出集合 A 中不同于集合 B 的元素，返回一个新的集合
# result = A - A&B
s1 = {1, 2, 3, 4, 5}
s2 = {2, 3 , 4, 7}

print(s1.difference(s2))

# A.difference_update(B) 从集合 A 中删除集合 B 中存在的元素，无返回值
# A = A - A&B
s1.difference_update(s2)
print(s1)

# A.union(B) 返回并集（新集合）
# result = A ｜ B
s1 = {1, 2, 3, 4, 5}
print(s1.union(s2))

# A.issubset(B) 判断 A 是否为 B 的子集
# result = True or False
s3 = {2, 3}

result = s3.issubset(s1)
print(result)

# A.issuperset(B) 判断 A 是否包含 B 
result = s1.issuperset(s3)
print(result)

# A.isdisjoint(B) 判断 A 与 B 是否没有交集 disjoint 脱节、不相交
result = s1.isdisjoint(s2)
print(result)