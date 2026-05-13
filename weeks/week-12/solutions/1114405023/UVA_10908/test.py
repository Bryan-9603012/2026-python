CASES = [('1\n7 10 4\nabbbaaaaaa\nabbbaaaaaa\nabbbaaaaaa\naaaaaaaaaa\naaaaaaaaaa\naaccaaaaaa\naaccaaaaaa\n1 2\n2 4\n4 6\n5 2\n', '7 10 4\n3\n1\n5\n1'), ('1\n3 3 2\naaa\naaa\naaa\n1 1\n0 0\n', '3 3 2\n3\n1')]

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
