import subprocess
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent
PROGRAMS = ["main.py", "simple_commented.py", "simple.py"]
SAMPLE_INPUT = '5\n1 10\n2 21\n3 8\n12 12\n1 1\n'
SAMPLE_EXPECTED = 'Monday\nMonday\nTuesday\nMonday\nSaturday\n'
EXTRA_INPUT = '4\n5 9\n8 8\n10 31\n12 25\n'
EXTRA_EXPECTED = 'Monday\nMonday\nMonday\nSunday\n'

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
