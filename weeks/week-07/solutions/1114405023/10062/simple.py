import sys


def solve(data: str) -> str:
    # 讀入所有數字
    data = data.strip().split()
    if not data:
        return ""

    # n = 牛的數量
    n = int(data[0])

    # smaller_before[i] = 第 i 個位置的牛，前面有幾頭編號比牠小
    # 題目只給第 2~n 個位置，所以第 1 個位置預設為 0
    smaller_before = [0] * (n + 1)
    for i in range(2, n + 1):
        smaller_before[i] = int(data[i - 1])

    # available 保存目前還沒被放入答案的編號
    # 因為編號是 1~n，所以一開始全部都可用
    available = list(range(1, n + 1))

    # ans[pos] = 第 pos 個位置的牛編號
    ans = [0] * (n + 1)

    # 從後面往前決定答案
    # 因為 smaller_before[pos] 代表在剩下的編號中，
    # 這頭牛是第 idx 小的那個
    for pos in range(n, 0, -1):
        idx = smaller_before[pos]
        ans[pos] = available.pop(idx)

    # 依照題目格式，每行輸出一個編號
    return "\n".join(map(str, ans[1:]))


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
