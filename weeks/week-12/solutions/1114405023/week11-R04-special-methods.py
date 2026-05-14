from functools import total_ordering

@total_ordering
class Score:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"Score({self.name!r}, {self.value})"

    def __eq__(self, other):
        if not isinstance(other, Score):
            return NotImplemented
        return self.value == other.value

    def __lt__(self, other):
        if not isinstance(other, Score):
            return NotImplemented
        return self.value < other.value

s1 = Score("Alice", 90)
s2 = Score("Bob", 75)
s3 = Score("Carol", 90)

print(s1 > s2)
print(s1 == s3)
print(s1 != s2)
print(sorted([s1, s2, s3]))

class Classroom:
    def __init__(self, name):
        self.name = name
        self._students = []

    def add(self, student):
        self._students.append(student)

    def __len__(self):
        return len(self._students)

    def __contains__(self, student):
        return student in self._students

    def __iter__(self):
        return iter(self._students)

    def __repr__(self):
        return f"Classroom({self.name!r}, {len(self)} 人)"

cls = Classroom("資工一甲")
cls.add("Alice")
cls.add("Bob")
cls.add("Carol")

print(len(cls))
print("Alice" in cls)
print("Dave" in cls)

for student in cls:
    print(student)
