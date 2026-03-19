def sequence_clean(nums):
    # 1. dedupe (保持第一次出現順序)
    seen = set()
    dedupe = []
    for n in nums:
        if n not in seen:
            seen.add(n)
            dedupe.append(n)

    # 2. 升序
    asc = sorted(nums)

    # 3. 降序
    desc = sorted(nums, reverse=True)

    # 4. 偶數
    evens = [n for n in nums if n % 2 == 0]

    return dedupe, asc, desc, evens


def main():
    nums = list(map(int, input().split()))

    dedupe, asc, desc, evens = sequence_clean(nums)

    print("dedupe:", *dedupe)
    print("asc:", *asc)
    print("desc:", *desc)
    print("evens:", *evens)


if __name__ == "__main__":
    main()