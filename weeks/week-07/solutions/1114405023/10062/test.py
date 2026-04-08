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

def build_case(perm):
    n = len(perm)
    rows = [str(n)]
    for i in range(1, n):
        cnt = sum(1 for j in range(i) if perm[j] < perm[i])
        rows.append(str(cnt))
    return "\n".join(rows) + "\n"

# Exhaustive small tests
for n in range(2, 8):
    for perm in itertools.permutations(range(1, n + 1)):
        data = build_case(perm)
        a = main.solve(data).strip()
        b = simple.solve(data).strip()
        assert a == b, (n, perm, a, b)

# Random bigger tests
for n in [10, 20, 50, 100]:
    for _ in range(50):
        perm = list(range(1, n + 1))
        random.shuffle(perm)
        data = build_case(perm)
        a = main.solve(data).strip()
        b = simple.solve(data).strip()
        assert a == b, (n, a, b)

print("10062: all tests passed")
