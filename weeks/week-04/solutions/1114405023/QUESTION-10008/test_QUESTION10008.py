from io import StringIO
import sys

def run_io_fun(input_data, func):
    backup_stdin = sys.stdin
    backup_stdout = sys.stdout

    sys.stdin = StringIO(input_data)
    sys.stdout = StringIO()

    func()

    output = sys.stdout.getvalue()

    sys.stdin = backup_stdin
    sys.stdout = backup_stdout

    return output


# ✅ 測試
def test():
    input_data = """3
This is a test
Count me in
Hello World
"""

    from QUESTION10008_me import solve  # ← 確認檔名

    output = run_io_fun(input_data, solve)
    print(output)


if __name__ == "__main__":
    test()