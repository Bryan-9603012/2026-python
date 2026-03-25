import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).with_name("10041.py")


def run_case(inp: str) -> str:
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=inp,
        text=True,
        capture_output=True,
        check=True
    )
    return result.stdout.strip()


def test_sample():
    inp = """2
2 2 4
3 2 4 6
"""
    assert run_case(inp) == "2\n4"


def test_unsorted_and_duplicates():
    inp = """2
5 10 2 2 9 7
4 1 1 1 1
"""
    assert run_case(inp) == "15\n0"


if __name__ == "__main__":
    test_sample()
    test_unsorted_and_duplicates()
    print("All tests passed.")