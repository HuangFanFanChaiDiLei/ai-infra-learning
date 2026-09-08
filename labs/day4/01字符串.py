msg = 'hello world hi'
# 字符串的字符不可修改
# msg[0] = 'H'  # 这行会引发错误

# index 方法, 返回下标
index = msg.index('o')  # 查找字符'o'在字符串中的索引位置
print(index)

# split 方法, 返回一个列表
result = msg.split(' ')
print(result)

# replace 方法, 将 字符串片段 替换成 目标字符串, 返回新字符串
result = msg.replace('hi','你好')
print(result)

# count 方法
print(msg.count('o'))

# strip 方法，从字符串中删除 指定字符串 的任意字符
# 从字符串左右两端开始删除，遇到第一个不在 指定字符串 中字符就停下
# 不修改原字符串，返回经过处理的新字符串

msg1 = '12234尚222硅111谷32114'
result = msg1.strip('1234')
print(msg1)
print(result)
