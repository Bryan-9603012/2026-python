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

fixed_data = """1 1
4 10
3 6
"""

assert main.solve(fixed_data).strip() == simple.solve(fixed_data).strip()

for s in range(1, 20):
    for d in range(1, 500):
        data = f"{s} {d}\n"
        a = main.solve(data).strip()
        b = simple.solve(data).strip()
        assert a == b, (s, d, a, b)

for _ in range(200):
    s = random.randint(1, 1000)
    d = random.randint(1, 10**7)
    ans = int(main.solve(f"{s} {d}\n").strip())
    # verify condition directly
    prev_total = (ans - 1) * ans // 2 - (s - 1) * s // 2 if ans - 1 >= s else 0
    cur_total = ans * (ans + 1) // 2 - (s - 1) * s // 2
    assert prev_total < d <= cur_total

print("10170: all tests passed")
