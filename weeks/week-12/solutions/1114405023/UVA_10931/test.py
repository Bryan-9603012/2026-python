CASES = [('1\n2\n10\n21\n0\n', 'The parity of 1 is 1 (mod 2).\nThe parity of 10 is 1 (mod 2).\nThe parity of 1010 is 2 (mod 2).\nThe parity of 10101 is 3 (mod 2).'), ('2147483647\n0\n', 'The parity of 1111111111111111111111111111111 is 31 (mod 2).')]

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_module(filename):
    path = ROOT / filename
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_cases(module_name, cases):
    module = load_module(module_name)
    for idx, (sample_input, expected_output) in enumerate(cases, 1):
        actual = module.solve(sample_input).strip()
        expected = expected_output.strip()
        assert actual == expected, (
            f"{module_name} case {idx} failed\n"
            f"Expected:\n{expected}\n\nActual:\n{actual}"
        )


def test_main():
    cases = CASES
    run_cases("main.py", cases)
    run_cases("main_optimized.py", cases)
    run_cases("main_optimized_clean.py", cases)


if __name__ == "__main__":
    test_main()
    print("All tests passed.")
