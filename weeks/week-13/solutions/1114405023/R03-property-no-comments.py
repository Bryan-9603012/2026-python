class BadStudent:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

s = BadStudent("王小明", 85)
s.grade = -100
print(f"糟糕：{s.name} 的成績是 {s.grade}")


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    @property
    def grade(self):
        """getter：讀取 self.grade 時呼叫"""
        return self._grade

    @grade.setter
    def grade(self, value):
        """setter：執行 self.grade = xxx 時呼叫"""
        if not (0 <= value <= 100):
            raise ValueError(f"成績必須在 0～100，你給了 {value}")
        self._grade = value

print("\n=== @property 守門員 ===")
s = Student("李大華", 90)
print(s.grade)

s.grade = 75
print(s.grade)

try:
    s.grade = -10
except ValueError as e:
    print(f"錯誤：{e}")


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        """面積是計算出來的，不該被直接設定"""
        import math
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

print("\n=== 唯讀屬性（計算值）===")
c = Circle(5)
print(f"半徑 {c.radius}，直徑 {c.diameter:.1f}，面積 {c.area:.2f}")

c.radius = 10
print(f"半徑 {c.radius}，直徑 {c.diameter:.1f}，面積 {c.area:.2f}")


class GradStudent(Student):

    @Student.grade.setter
    def grade(self, value):
        if not (0 <= value <= 150):
            raise ValueError(f"研究生成績必須在 0～150，你給了 {value}")
        self._grade = value

print("\n=== 子類覆寫 setter ===")
g = GradStudent("張教授", 120)
print(g.grade)


