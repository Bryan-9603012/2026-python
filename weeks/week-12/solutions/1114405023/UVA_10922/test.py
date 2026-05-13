CASES = [('999999999999999999999\n9\n18\n123\n0\n', '999999999999999999999 is a multiple of 9 and has 9-degree 3.\n9 is a multiple of 9 and has 9-degree 1.\n18 is a multiple of 9 and has 9-degree 1.\n123 is not a multiple of 9.'), ('999\n1000\n0\n', '999 is a multiple of 9 and has 9-degree 2.\n1000 is not a multiple of 9.')]

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
