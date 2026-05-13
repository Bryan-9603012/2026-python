CASES = [('112233\n30800\n2937\n323455693\n12345\n0\n', '112233 is a multiple of 11.\n30800 is a multiple of 11.\n2937 is a multiple of 11.\n323455693 is a multiple of 11.\n12345 is not a multiple of 11.'), ('11\n12\n121\n0\n', '11 is a multiple of 11.\n12 is not a multiple of 11.\n121 is a multiple of 11.')]

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
