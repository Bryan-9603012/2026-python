CASES = [('2\n40 20\n20 40\n', '30 10\nimpossible'), ('4\n0 0\n1 1\n5 2\n10 4\n', '0 0\n1 0\nimpossible\n7 3')]

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
