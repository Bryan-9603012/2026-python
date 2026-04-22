import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).with_name('main.py')

def run_case(inp: str) -> str:
    return subprocess.run([sys.executable, str(SCRIPT)], input=inp, text=True, capture_output=True, check=True).stdout

def test_sample():
    inp = "3\n0\n0\n0\n3\n1 0\n3 0\n0\n"
    expected = "ABC\nCB\nBAC\nCA\nCAB\nBA\n\nBAC\nCA\nCBA"
    assert run_case(inp).strip() == expected

def test_single_person():
    assert run_case("1\n0\n").strip() == 'A'
