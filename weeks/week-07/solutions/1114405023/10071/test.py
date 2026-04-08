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

fixed_cases = [
    [0],
    [1],
    [-1, 0, 1],
    [1, 2, 3],
    [-2, -1, 1, 2],
]

def build_case(arr):
    return str(len(arr)) + "\n" + "\n".join(map(str, arr)) + "\n"

for arr in fixed_cases:
    data = build_case(arr)
    a = main.solve(data).strip()
    b = simple.solve(data).strip()
    assert a == b, (arr, a, b)

for n in range(1, 6):
    for _ in range(60):
        arr = random.sample(range(-5, 6), n)
        data = build_case(arr)
        a = main.solve(data).strip()
        b = simple.solve(data).strip()
        assert a == b, (arr, a, b)

print("10071: all tests passed")
