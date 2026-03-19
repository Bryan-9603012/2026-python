def student_ranking(students, k):
    ranked = sorted(
        students,
        key=lambda x: (-x[1], x[2], x[0])
    )
    return ranked[:k]


def main():
    n, k = map(int, input().split())

    students = []
    for _ in range(n):
        name, score, age = input().split()
        students.append((name, int(score), int(age)))

    result = student_ranking(students, k)

    for r in result:
        print(r[0], r[1], r[2])


if __name__ == "__main__":
    main()