import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).with_name('main.py')

def run_case(inp: str) -> str:
    return subprocess.run([sys.executable, str(SCRIPT)], input=inp, text=True, capture_output=True, check=True).stdout.strip()

def test_collinear_three_points():
    assert run_case("1\n3\n0 0\n1 1\n2 2\n") == '4 1'

def test_even_case_rectangle_of_optima():
    assert run_case("1\n2\n0 0\n2 2\n") == '4 9'
