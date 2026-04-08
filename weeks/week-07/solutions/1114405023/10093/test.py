import random
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def load(name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

main = load("main")
simple = load("simple")

fixed = [
    ["P"],
    ["PP"],
    ["PH", "HP"],
    ["PPP", "PPP"],
    ["PHP", "PPP", "HPH"],
]

def build_case(board):
    return f"{len(board)} {len(board[0])}\n" + "\n".join(board) + "\n"

for board in fixed:
    data = build_case(board)
    a = main.solve(data).strip()
    b = simple.solve(data).strip()
    assert a == b, (board, a, b)

for n in range(1, 5):
    for m in range(1, 6):
        for _ in range(80):
            board = []
            for _r in range(n):
                row = ''.join(random.choice("PH") for _ in range(m))
                board.append(row)
            data = build_case(board)
            a = main.solve(data).strip()
            b = simple.solve(data).strip()
            assert a == b, (board, a, b)

print("10093: all tests passed")
