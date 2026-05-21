print("=== with 開檔：自動關閉 ===")
with open("/tmp/week13_demo.txt", "w") as f:
    f.write("Hello from Week 13\n")

with open("/tmp/week13_demo.txt", "r") as f:
    print(f.read().strip())


import time

class Timer:
    """計時器：進入 with 時開始，離開時印出經過時間"""

    def __enter__(self):
        self.start = time.time()
        print("⏱  開始計時")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start
        print(f"⏱  結束：{elapsed:.4f} 秒")
        return False

print("\n=== 自訂計時器 ===")
with Timer() as t:
    total = sum(range(1_000_000))
print(f"計算結果：{total}")


from contextlib import contextmanager

@contextmanager
def section(title):
    """印出有邊框的區段標題"""
    print(f"\n{'='*40}")
    print(f"  {title}")
    print(f"{'='*40}")
    yield
    print(f"{'─'*40}")

print()
with section("Week 13 CPE 模擬考"):
    print("  題目：UVA 11005 Cheapest Base")
    print("  時間限制：20 分鐘")


import io, sys

@contextmanager
def capture_output():
    """暫時把 print 的輸出截取到字串裡"""
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    try:
        yield buffer
    finally:
        sys.stdout = old_stdout

def solve_parity(n):
    """UVA 10931 Parity：計算 n 的二進位裡有幾個 1"""
    bits = bin(n)[2:]
    ones = bits.count('1')
    print(f"The parity of {bits} is {ones} (mod 2 is {ones % 2}).")

print("\n=== 截取輸出（測試用）===")
with capture_output() as out:
    solve_parity(10)
    solve_parity(7)

captured = out.getvalue()
print("截取到的輸出：")
print(captured)


lines = captured.strip().split('\n')
print(f"共 {len(lines)} 行輸出")


