import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).with_name('main.py')

def run_case(inp: str) -> str:
    return subprocess.run([sys.executable, str(SCRIPT)], input=inp, text=True, capture_output=True, check=True).stdout.strip()

def test_single_open_cell():
    assert run_case("1\n1 1\n1\n") == 'Case 1: 0'

def test_single_socket_cell():
    assert run_case("1\n1 1\n0\n") == 'Case 1: 1'

def test_two_open_cells_line():
    assert run_case("1\n1 2\n1 1\n") == 'Case 1: 1'
