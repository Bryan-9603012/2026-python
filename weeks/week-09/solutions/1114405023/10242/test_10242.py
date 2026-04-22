import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).with_name('main.py')

def run_case(inp: str) -> str:
    return subprocess.run([sys.executable, str(SCRIPT)], input=inp, text=True, capture_output=True, check=True).stdout.strip()

def test_simple_path():
    assert run_case("3 2\n1 2\n2 3\n10\n20\n30\n1 1\n3\n") == '60'

def test_scc_cycle_then_bar():
    assert run_case("4 4\n1 2\n2 1\n2 3\n3 4\n5\n7\n11\n13\n1 1\n4\n") == '36'
