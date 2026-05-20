"""自動測試 11005 - Cheapest Base"""
import subprocess
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

test_cases = [
    {
        "name": "Test 1: all costs=1, N=1",
        "input": "1\n" + " ".join(["1"] * 36) + "\n1\n1\n",
        "expected": "Case 1:\nCheapest base(s) for number 1: 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36\n"
    },
    {
        "name": "Test 2: costs vary, N=10",
        "input": "1\n" + " ".join(["1"] * 10) + " " + " ".join(["100"] * 26) + "\n1\n10\n",
        "expected": "Case 1:\nCheapest base(s) for number 10: 4 5 6 7 8 9 10\n"
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
