# sorted(), 返回值是新容器，原容器不变
# 与 sort 方法相同，默认 reverse=False 升序， 降序为 reverse=True
nums = [3, 1, 4, 2]
sorted_nums = sorted(nums)  # 升序排序
print(sorted_nums)  # 输出: [1, 2, 3, 4]
print(nums)  # 输出: [3, 1, 4, 2] (原列表不变)

# len(), 返回值是容器中元素的个数
# max(), 返回值是容器中元素的最大值
# min(), 返回值是容器中元素的最小值
# sum(), 返回值是容器中元素的总和