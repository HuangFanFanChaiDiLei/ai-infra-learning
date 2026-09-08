import sys
# 当数据很大时，我们可以使用下划线将数字进行分组，来让数字变得更加易读
house_price = 1_000_000
print('房子价格是', house_price)


# 打印数字时，print 会把数字转换为字符串进行打印
# 默认限制数字不能超过 4300 位
a = 9 ** 9999
b = a + 10
sys.set_int_max_str_digits(0)
print('a', a)