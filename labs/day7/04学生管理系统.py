# 学生管理系统（终端版）
# 功能：
#   1. 添加学生
#   2. 删除学生
#   3. 查看所有学生
#   4. 管理员功能（录入成绩 / 修改成绩）
#   0. 退出
# 说明：成绩默认是 None，代表还没有录入。
#       只有输入正确管理员密码后，才能录入 / 修改成绩。

# 管理员密码（可以自行修改）
ADMIN_PASSWORD = "123456"

# 用列表保存所有学生，每个学生是一个字典，字段固定：id / name / score
students = []

# 用来生成递增的学号
next_id = 1


def make_id():
    """生成一个新的学号（递增）。"""
    global next_id
    new_id = next_id
    next_id += 1
    return new_id


def add_student():
    """添加一个学生：只需要学号、姓名，成绩默认为空。"""
    global students
    name = input("请输入学生姓名：").strip()
    if name == "":
        print("❌ 姓名不能为空！")
        return

    student = {
        "id": make_id(),
        "name": name,
        "score": None,   # 成绩还没录入
    }
    students.append(student)
    print(f"✅ 添加成功！学号为 {student['id']} 的学生【{name}】已加入系统。")


def delete_student():
    """按学号删除一个学生。"""
    global students
    sid = _input_id("请输入要删除的学号：")
    if sid is None:
        return

    for i, stu in enumerate(students):
        if stu["id"] == sid:
            students.pop(i)
            print(f"✅ 已删除学号为 {sid} 的学生【{stu['name']}】。")
            return

    print(f"❌ 找不到学号为 {sid} 的学生。")


def show_all():
    """查看所有学生及其成绩。"""
    if not students:
        print("📭 系统里还没有任何学生，请先添加。")
        return

    print("\n" + "=" * 46)
    print("学号".ljust(6) + "姓名".ljust(10) + "成绩")
    print("-" * 46)
    for stu in students:
        # 成绩为空显示"未录入"，否则显示分数
        score = "未录入" if stu["score"] is None else f"{stu['score']}"
        print(str(stu["id"]).ljust(8) + stu["name"].ljust(10) + score)
    print("=" * 46)
    print(f"当前共有 {len(students)} 名学生。\n")


# ---------- 管理员相关 ----------

def is_admin():
    """校验管理员密码。"""
    password = input("请输入管理员密码：")
    if password == ADMIN_PASSWORD:
        print("✅ 密码正确，进入管理员模式。")
        return True
    print("❌ 密码错误，无法进入管理员功能。")
    return False


def input_score(sid):
    """录入/修改某个学生的成绩。返回 True 表示操作成功。"""
    for stu in students:
        if stu["id"] == sid:
            try:
                score = float(input(f"请输入学号 {sid}（{stu['name']}）的成绩："))
            except ValueError:
                print("❌ 成绩必须是数字！")
                return False
            if score < 0 or score > 100:
                print("❌ 成绩必须在 0~100 之间！")
                return False
            stu["score"] = score
            print(f"✅ 已录入/修改：{stu['name']} 的成绩为 {score} 分。")
            return True

    print(f"❌ 找不到学号为 {sid} 的学生。")
    return False


def record_score():
    """录入成绩。"""
    show_all()
    if not students:
        return
    sid = _input_id("请输入要录入成绩的学号：")
    if sid is not None:
        input_score(sid)


def modify_score():
    """修改成绩。"""
    if not students:
        print("📭 系统里还没有任何学生，请先添加。")
        return
    show_all()
    sid = _input_id("请输入要修改成绩的学号：")
    if sid is not None:
        input_score(sid)


def admin_menu():
    """管理员菜单：录入成绩 / 修改成绩 / 退出。"""
    if not is_admin():
        return

    while True:
        print("\n------ 管理员模式 ------")
        print("1. 录入成绩")
        print("2. 修改成绩")
        print("0. 退出管理员模式")
        choice = input("请选择：").strip()

        if choice == "1":
            record_score()
        elif choice == "2":
            modify_score()
        elif choice == "0":
            print("✅ 已退出管理员模式。")
            break
        else:
            print("❌ 无效选项，请重新输入。")


# ---------- 通用工具 ----------

def _input_id(tip):
    """输入学号，非法输入返回 None。"""
    try:
        return int(input(tip))
    except ValueError:
        print("❌ 学号必须是数字！")
        return None


# ---------- 主菜单 ----------

def main_menu():
    print("\n======== 学生管理系统 ========")
    print("1. 添加学生")
    print("2. 删除学生")
    print("3. 查看所有学生")
    print("4. 管理员功能（录入/修改成绩）")
    print("0. 退出系统")
    print("=" * 30)


def main():
    print("🎓 欢迎使用学生管理系统（终端版）！")
    while True:
        main_menu()
        choice = input("请选择功能：").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            delete_student()
        elif choice == "3":
            show_all()
        elif choice == "4":
            admin_menu()
        elif choice == "0":
            print("👋 感谢使用，再见！")
            break
        else:
            print("❌ 无效选项，请重新输入。")


# 程序入口
if __name__ == "__main__":
    main()
