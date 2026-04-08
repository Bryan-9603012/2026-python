import random
import itertools
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
    "1+1=2#",
    "8-3=9#",
    "9+0=9#",
    "5+3=9#",
    "10-7=3#",
    "7+7=8#",
]

for case in fixed_cases:
    a = main.solve(case).strip()
    b = simple.solve(case).strip()
    assert a == b, (case, a, b)

digits = '0123456789'
ops = ['+', '-']

def random_expr():
    left_terms = random.randint(1, 3)
    right_terms = random.randint(1, 3)

    def build(side_terms):
        s = ""
        for i in range(side_terms):
            if i == 0 and random.random() < 0.25:
                s += "-"
            elif i > 0:
                s += random.choice(ops)
            num_len = random.randint(1, 3)
            first = random.choice('123456789')
            rest = ''.join(random.choice(digits) for _ in range(num_len - 1))
            s += first + rest
        return s

    return build(left_terms) + "=" + build(right_terms) + "#"

for _ in range(400):
    case = random_expr()
    a = main.solve(case).strip()
    b = simple.solve(case).strip()
    assert a == b, (case, a, b)

print("10101: all tests passed")
