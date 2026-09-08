# range()函数可以生成一个整数序列，常用于for循环中
# range(10) = range(0, 10) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# end 是 print 的命名参数，控制打印结束后输出什么字符
# 默认：print() 默认 end='\n'，也就是打印完自动换行
# end=' '：打印完，不换行，输出一个空格
# for n in range(10):
#     print(n, end=' ')

# print() # 换行
# for n in range(1, 11):
#     print(n, end=' ')

# print() # 换行
# for n in 'abcdef':
#     print(n, end=' ')


text = input('请输入一段文字：')
secret = ''
for ch in text:
    unicode = ord(ch) # 获取字符的 Unicode 编码
    secret += chr(unicode + 1) # 将 Unicode 编码加 1 后转换为字符，并拼接到 secret 中
print(f'加密后的文字是：{secret}')

mingwen = ''
for ch in secret:
    unicode = ord(ch)
    mingwen += chr(unicode - 1)
print(f'解密后的文字是：{mingwen}')