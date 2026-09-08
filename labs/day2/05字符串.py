# `\` 叫行继续符（续行符）
# 所以 VS Code / Pylance 在你回车的时候，
# 自动补 `\` 告诉解释器：这一行没结束，下一行是同一语句

message1 = 'hello ' \
'world'

# 括号隐式续行，推荐，不用反斜杠
message2 = ("hello "
            "world")

# 三引号，保留真实换行（字符串内部带 \n）
message3 = '''hello
world'''
message4 = """hello world"""

print(message1)
print(message2)
print(message3)
print(message4)