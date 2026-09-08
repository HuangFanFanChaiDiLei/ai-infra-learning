nums = [62, 50, 60, 48, 80, 20, 99]

for index in range(len(nums)):
    print(f"索引: {index}, 元素: {nums[index]}")

for item in nums:
    print(f"元素: {item}")

# start 控制的是遍历时的 index 起始值，默认是0
# 并不会改变列表中的实际索引值
for index, item in enumerate(nums, start=3):
    print(f"索引: {index}, 元素: {item}")
