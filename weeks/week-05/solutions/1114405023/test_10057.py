import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).with_name("10057.py")


def run_case(inp: str) -> str:
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=inp,
        text=True,
        capture_output=True,
        check=True
    )
    return result.stdout.strip()


def test_odd_count():
    inp = """5
1 2 3 4 5
"""
    assert run_case(inp) == "3 1 1"


def test_even_count_with_range_of_answers():
    inp = """4
1 2 2 3
"""
    assert run_case(inp) == "2 2 1"


def test_even_count_multiple_possible_answers():
    inp = """4
1 2 4 5
"""
    assert run_case(inp) == "2 2 3"


if __name__ == "__main__":
    test_odd_count()
    test_even_count_with_range_of_answers()
    test_even_count_multiple_possible_answers()
    print("All tests passed.")