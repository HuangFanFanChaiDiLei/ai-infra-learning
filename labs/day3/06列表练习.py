print('请输入学生成绩，输入“done”结束输入：')

scores = list()

while True:
    sore = input('请输入成绩：')
    if sore == 'done':
        break
    elif not sore.isdigit() or not (0 <= int(sore) <= 100):
        print("输入无效，请输入0-100之间的数字。")
    else:
        scores.append(int(sore))

if scores: 
    length = len(scores)
    print(f"总人数为：{length}")
    print(f"最高成绩为: {max(scores)}")
    print(f"最低成绩为: {min(scores)}")
    average_score = sum(scores) / len(scores)
    print(f"平均成绩为: {average_score:.2f}")
    pass_count = 0
    excellent_count = 0
    for score in scores:
        if score >= 60:
            pass_count += 1
        if score >= 90:
            excellent_count += 1
    print(f"及格人数: {pass_count}")
    print(f"及格率为: {pass_count / length * 100:.2f}%")
    print(f"优秀人数: {excellent_count}")
    print(f"优秀率为: {excellent_count / length * 100:.2f}%")
else:
    print("没有输入有效的成绩。")