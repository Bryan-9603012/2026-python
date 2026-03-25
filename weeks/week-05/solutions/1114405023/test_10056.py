import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).with_name("10056.py")


def run_case(inp: str) -> str:
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input=inp,
        text=True,
        capture_output=True,
        check=True
    )
    return result.stdout.strip()


def test_sample_style():
    inp = """3
3 0.1666666667 1
3 0.1666666667 2
3 0.1666666667 3
"""
    assert run_case(inp) == "0.3956\n0.3297\n0.2747"


def test_zero_probability():
    inp = """1
5 0.0 3
"""
    assert run_case(inp) == "0.0000"


if __name__ == "__main__":
    test_sample_style()
    test_zero_probability()
    print("All tests passed.")