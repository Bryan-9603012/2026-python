import sys

# 將輸入中的 = 換成空白，方便解析 N = n
tokens = sys.stdin.read().replace("=", " ").split()
t = int(tokens[0])
idx = 1

for case_id in range(1, t + 1):
    # 略過字串 N
    if tokens[idx] == "N":
        idx += 1

    # 讀取矩陣大小
    n = int(tokens[idx])
    idx += 1

    # 將矩陣攤平成一維陣列
    values = list(map(int, tokens[idx:idx + n * n]))
    idx += n * n

    # 中心對稱等價於一維陣列前後對照相同
    ok = True
    left = 0
    right = len(values) - 1

    while left <= right:
        # 只要有負數，或中心對稱位置不相等，就不是 Symmetric
        if values[left] < 0 or values[right] < 0 or values[left] != values[right]:
            ok = False
            break
        left += 1
        right -= 1

    print(f"Test #{case_id}: {'Symmetric.' if ok else 'Non-symmetric.'}")
