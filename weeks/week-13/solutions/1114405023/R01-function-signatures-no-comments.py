def add_all(*args):
    """args 在函數內是一個 tuple"""
    return sum(args)

print("=== *args：不定個數的位置參數 ===")
print(add_all(1, 2))
print(add_all(1, 2, 3, 4, 5))
print(add_all())


def make_student(**kwargs):
    """建立學生資料，欄位可以自由指定"""
    return kwargs

print("\n=== **kwargs：不定個數的關鍵字參數 ===")
s = make_student(name="王小明", grade=85, seat=12)
print(s)


def send_score(student_id, *, subject, score):
    """* 之後的參數必須具名，避免搞混"""
    print(f"學號 {student_id}｜{subject}：{score} 分")

print("\n=== keyword-only：強制具名，避免填錯順序 ===")
send_score("411234001", subject="數學", score=90)


def report(title, *scores, prefix="成績"):
    """title 普通參數，scores 不定個數，prefix 有預設值"""
    avg = sum(scores) / len(scores) if scores else 0
    print(f"{prefix}報告－{title}：平均 {avg:.1f}")

print("\n=== 混合：普通 + *args + 預設值 ===")
report("期中考", 80, 90, 70)
report("期末考", 95, 85, 75, 100, prefix="最終")


