num1 = 0b11001 # binary
num2 = 0o1034 # octal
num3 = 0x1AF # hexadecimal

# python中所有的非十进制数字，只是代码层面的编写方式
# 是给程序员看的，最终在内存中存储的都是十进制数字
print(num1, num2, num3)

# bin 十进制 数字 二进制 字符串
# oct 十进制 数字 转八进制 字符串
# hex 十进制 数字 转十六进制 字符串
print(bin(num1), oct(num2), hex(num3))
# int 二进制、八进制、十六进制的 字符串 转十进制 数字
print(int('0b11001', 2), int('0o1034', 8), int('0x1AF', 16))