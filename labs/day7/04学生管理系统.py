from datetime import datetime


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Student(Person):
    count = 1  # 类属性：用来生成递增且唯一的学号

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        # 学号 = 入学年份 + 序号，每新增一个学生 count 就 +1，保证不重复
        self.id = f'{datetime.now().year}{Student.count:03d}'
        Student.count += 1
        self.scores = {}

    # 录入 / 修改成绩（key 相同时直接覆盖旧成绩，达到"修改"效果）
    def set_score(self, subject, score):
        self.scores[subject] = score

    # 删除某科成绩
    def del_score(self, subject):
        self.scores.pop(subject, None)

    # 返回平均成绩（没成绩返回 0）
    def get_average_score(self):
        if self.scores:
            return sum(self.scores.values()) / len(self.scores)
        return 0

    # 重写 __str__ 魔法方法
    def __str__(self):
        return (f'[{self.id}] {self.name} | {self.age}岁 | {self.gender}'
                f' | 成绩:{self.scores} | 平均:{self.get_average_score():.1f}')


# 管理 Student 实例
class Manager:
    def __init__(self):
        self.students = []

    # 根据学号查找学生，找不到返回 None
    def find_student(self, sid):
        for student in self.students:
            if sid == student.id:
                return student
        return None

    # 添加学生
    def add_student(self, student):
        self.students.append(student)

    # 按学号删除学生，成功返回 True
    def del_student(self, sid):
        student = self.find_student(sid)
        if student:
            self.students.remove(student)
            return True
        return False

    # 展示所有学生
    def show_all_students(self):
        if not self.students:
            print('系统内暂无学生')
            return
        for student in self.students:
            print(student)

    # 主菜单
    def run(self):
        while True:
            print('\n--------学生管理系统--------')
            print('1.添加学生')
            print('2.删除学生')
            print('3.查看所有学生')
            print('4.录入/修改成绩')
            print('5.退出')

            choice = self._input_int('请输入序列号：', '请输入菜单序号')

            if choice == 1:
                name = input('请输入学生姓名：').strip()
                if not name:
                    print('❌ 姓名不能为空')
                    continue
                age = self._input_int('请输入学生年龄：', '请输入数字年龄')
                gender = input('请输入学生性别：').strip()
                student = Student(name, age, gender)
                self.add_student(student)
                print(f'✅ 添加成功，学号：{student.id}')
            elif choice == 2:
                if not self.students:
                    print('系统内暂无学生')
                    continue
                sid = input('请输入要删除的学生学号：').strip()
                if self.del_student(sid):
                    print(f'✅ 已删除学号 {sid} 的学生')
                else:
                    print(f'❌ 学号 {sid} 不存在')
            elif choice == 3:
                self.show_all_students()
            elif choice == 4:
                self._set_score_flow()
            elif choice == 5:
                print('👋 感谢使用，再见')
                break
            else:
                print('❌ 序列号非法，请重新输入')

    # 录入/修改成绩流程：按学号定位 -> 录入科目与分数
    def _set_score_flow(self):
        if not self.students:
            print('系统内暂无学生，请先添加')
            return
        self.show_all_students()
        sid = input('请输入要录入成绩的学生学号：').strip()
        student = self.find_student(sid)
        if not student:
            print(f'❌ 学号 {sid} 不存在')
            return

        # 展示该生现有成绩，方便判断是新增还是修改
        print(f'{student.name} 当前成绩：{student.scores if student.scores else "（暂无）"}')
        subject = input('请输入学科：').strip()
        if not subject:
            print('❌ 学科不能为空')
            return
        score = self._input_score()
        student.set_score(subject, score)
        print(f'✅ 已为 {student.name} 录入 {subject}：{score} 分')

    # 读取 0~100 的成绩
    def _input_score(self):
        while True:
            value = self._input_int('请输入成绩（0~100）：', '请输入数字成绩')
            if 0 <= value <= 100:
                return value
            print('❌ 成绩必须在 0~100 之间')

    # 读取整数的通用函数，输入非法时不会崩溃，而是要求重新输入
    @staticmethod
    def _input_int(prompt, err_tip):
        while True:
            raw = input(prompt).strip()
            try:
                return int(raw)
            except ValueError:
                print(f'❌ {err_tip}，请重新输入')


if __name__ == '__main__':
    Manager().run()
