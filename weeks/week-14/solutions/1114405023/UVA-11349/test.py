import subprocess
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent
PROGRAMS = ["main.py", "simple_commented.py", "simple.py"]
SAMPLE_INPUT = '2\nN = 3\n5 1 3\n2 0 2\n3 1 5\nN = 3\n5 1 3\n2 0 2\n0 1 5\n'
SAMPLE_EXPECTED = 'Test #1: Symmetric.\nTest #2: Non-symmetric.\n'
EXTRA_INPUT = '3\nN = 1\n0\nN = 2\n1 2\n2 1\nN = 2\n1 -2\n-2 1\n'
EXTRA_EXPECTED = 'Test #1: Symmetric.\nTest #2: Symmetric.\nTest #3: Non-symmetric.\n'

def norm(s):
    return s.strip().replace("\r\n", "\n")

def run(program, input_data):
    r = subprocess.run([sys.executable, str(ROOT/program)], input=input_data, text=True, capture_output=True, check=True, timeout=10)
    return r.stdout

def check(program, name, input_data, expected):
    actual = run(program, input_data)
    if norm(actual) != norm(expected):
        raise AssertionError(f"{program} failed {name}\nExpected:\n{expected}\nActual:\n{actual}")

def main():
    for program in PROGRAMS:
        check(program, "sample", SAMPLE_INPUT, SAMPLE_EXPECTED)
        check(program, "extra", EXTRA_INPUT, EXTRA_EXPECTED)
    print("All tests passed.")

if __name__ == "__main__":
    main()
