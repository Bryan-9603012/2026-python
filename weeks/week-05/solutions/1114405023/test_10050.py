import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).with_name("10050.py")


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
    inp = """1
14
3
3
4
8
"""
    assert run_case(inp) == "5"


def test_multiple_parties_overlap():
    inp = """1
30
3
3
4
8
"""
    assert run_case(inp) == "10"


if __name__ == "__main__":
    test_sample()
    test_multiple_parties_overlap()
    print("All tests passed.")