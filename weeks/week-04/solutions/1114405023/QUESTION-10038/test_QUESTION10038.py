from io import StringIO
import sys
from QUESTION10038_me import solve

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
    input_data = """4 1 4 2 3
5 1 4 2 -1 6
"""
    output = run_io_fun(input_data, solve)

    print("=== OUTPUT ===")
    print(output)

if __name__ == "__main__":
    test()