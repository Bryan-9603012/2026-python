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


def test():
    input_data = """1

4 2
1 1 2
<
1 3 4
=
"""

    from QUESTION948_me import solve  # ⚠️ 檔名要正確

    output = run_io_fun(input_data, solve)

    print("=== OUTPUT ===")
    print(output)


if __name__ == "__main__":
    test()   # ⭐ 一定要呼叫