import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).with_name("10055.py")


def run_case(inp: str) -> str:
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=inp,
        text=True,
        capture_output=True,
        check=True
    )
    return result.stdout.strip()


def test_basic_toggle_and_query():
    inp = """5 6
2 1 5
1 3
2 1 5
1 5
2 3 5
2 4 4
"""
    assert run_case(inp) == "0\n1\n0\n0"


def test_retoggle_same_index():
    inp = """3 5
1 2
2 1 3
1 2
2 1 3
2 2 2
"""
    assert run_case(inp) == "1\n0\n0"


if __name__ == "__main__":
    test_basic_toggle_and_query()
    test_retoggle_same_index()
    print("All tests passed.")