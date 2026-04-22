import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).with_name('main.py')

def run_case(inp: str) -> str:
    return subprocess.run([sys.executable, str(SCRIPT)], input=inp, text=True, capture_output=True, check=True).stdout.strip()

def test_one_egg():
    assert run_case("1 10\n0 0\n") == '10'

def test_two_eggs():
    assert run_case("2 100\n0 0\n") == '14'

def test_more_than_63():
    assert run_case("1 1000000000000000000\n0 0\n") == 'More than 63 trials needed.'
