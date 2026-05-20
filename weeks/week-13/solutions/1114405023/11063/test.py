"""自動測試 11063 - RGB to XYZ"""
import subprocess
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

test_cases = [
    {
        "name": "Test 1: 2x2 image with pure colors",
        "input": "2\n255 0 0 0 255 0\n0 0 255 128 128 128\n",
        "expected": (
            "131.2995 67.6770 6.3240\n"
            "82.7220 170.9520 31.8240\n"
            "40.9785 16.3710 216.8520\n"
            "128.0000 128.0000 128.0000\n"
            "The average of Y is 95.7500\n"
        )
    },
    {
        "name": "Test 2: 1x1 image (single pixel black)",
        "input": "1\n0 0 0\n",
        "expected": (
            "0.0000 0.0000 0.0000\n"
            "The average of Y is 0.0000\n"
        )
    },
]


def run_test(script, test_input, expected):
    try:
        result = subprocess.run(
            [sys.executable, script],
            input=test_input,
            capture_output=True,
            text=True,
            timeout=10
        )
        actual = result.stdout
        if actual.strip() == expected.strip():
            return True, actual
        return False, actual
    except Exception as e:
        return False, str(e)


def main():
    log_lines = []
    all_pass = True

    for script_name in ["main.py", "main_simple.py"]:
        script_path = os.path.join(SCRIPT_DIR, script_name)
        log_lines.append(f"=== Testing {script_name} ===")

        for tc in test_cases:
            log_lines.append(f"\n--- {tc['name']} ---")
            passed, actual = run_test(script_path, tc["input"], tc["expected"])
            if passed:
                log_lines.append("PASS")
            else:
                log_lines.append("FAIL")
                log_lines.append(f"Expected:\n{tc['expected']}")
                log_lines.append(f"Actual:\n{actual}")
                all_pass = False

        log_lines.append("")

    status = "ALL PASS" if all_pass else "SOME FAIL"
    log_lines.append(f"Overall: {status}")

    log_text = "\n".join(log_lines)
    print(log_text)

    with open(os.path.join(SCRIPT_DIR, "log.txt"), "w") as f:
        f.write(log_text + "\n")

    if not all_pass:
        sys.exit(1)


if __name__ == "__main__":
    main()
