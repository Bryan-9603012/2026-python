## Project

6/11 Sort Lab — Sorting Algorithm Benchmark

## Environment

* OS: Windows
* Python command used for final test: `py`
* Test framework: `unittest`
* Plot dependency: `matplotlib`

---

## Stage 2 — Sorting Algorithm Tests

### Test File

```text
test_sorts.py
```

### Target Files

```text
sorts.py
```

### Tested Functions

```python
bubble_sort(data: list) -> list
quick_sort(data: list) -> list
merge_sort(data: list) -> list
```

After Stage 3, the same correctness tests were also applied to:

```python
builtin_sorted(data: list) -> list
optimized_quick_sort(data: list) -> list
```

### Test Cases

The sorting tests covered the following cases:

1. Normal integer list
2. Empty list
3. Single-element list
4. Already sorted list
5. Reverse sorted list
6. List with duplicate values
7. List with negative numbers
8. Original input list should not be modified
9. Invalid input should raise `TypeError`

### Red Light Result

Before `sorts.py` was implemented, the test failed because the module did not exist.

```text
ModuleNotFoundError: No module named 'sorts'
```

This confirmed that the test entered the expected red-light state.

### Green Light Result

After implementing the three sorting algorithms, the tests passed.

```text
Ran 9 tests in 0.004s

OK
```

---

## Stage 3 — Benchmark and Optimized Sorting Tests

### Target Files

```text
sorts.py
benchmark.py
results.json
```

### Added Sorting Methods

```python
builtin_sorted(data: list) -> list
optimized_quick_sort(data: list) -> list
```

### Red Light Result

After adding `builtin_sorted` and `optimized_quick_sort` to the shared sorting tests, the test failed because the new functions were not implemented yet.

```text
ImportError: cannot import name 'builtin_sorted' from 'sorts'
```

This confirmed that the Stage 3 test entered the expected red-light state.

### Green Light Result

After implementing the baseline and optimized quick sort, all sorting correctness tests passed.

### Benchmark Command

```bash
python benchmark.py
```

### Benchmark Result

```text
Size      bubble_sort              quick_sort               merge_sort              builtin_sorted           optimized_quick_sort
500       0.015886                 0.000830                 0.001907                0.000062                 0.001026
1000      0.082816                 0.001976                 0.003559                0.000097                 0.001452
2000      0.413051                 0.003571                 0.007382                0.000226                 0.003646
4000      1.717670                 0.007698                 0.017615                0.000625                 0.007525
```

### Observation

* `bubble_sort` was the slowest method.
* `builtin_sorted` was the fastest method overall.
* `optimized_quick_sort` slightly improved over the original `quick_sort` at size `4000`.
* At size `4000`, the optimized version improved from `0.007698` seconds to `0.007525` seconds.

### Speed Improvement Calculation

```text
(0.007698 - 0.007525) / 0.007698 * 100 ≈ 2.25%
```

---

## Stage 4 — Plot Generation Test

### Test File

```text
test_plot.py
```

### Target File

```text
plot.py
```

### Output File

```text
assets/benchmark.png
```

### Test Goal

The plot test verified that:

1. `plot_benchmark()` can read `results.json`.
2. `assets/benchmark.png` is created successfully.
3. The generated PNG file is not empty.

### Red Light Result

Before `plot.py` was implemented, the test failed because the module did not exist.

```text
ModuleNotFoundError: No module named 'plot'
```

This confirmed that the Stage 4 test entered the expected red-light state.

### Environment Issue

After creating `plot.py`, one Python environment failed because `matplotlib` was not installed.

```text
ModuleNotFoundError: No module named 'matplotlib'
```

The issue was caused by using different Python commands:

```text
python
py
```

The final tests were run successfully using:

```bash
py -m unittest
```

### Green Light Result

```text
Ran 1 test in 0.909s
OK
```

### Generated Plot

```text
assets/benchmark.png
```

The plot uses log scale on the y-axis to compare the runtime differences between sorting methods.

---

## Stage 5 — Security and Validation Tests

### Test File

```text
test_security.py
```

### Target File

```text
benchmark.py
```

### Security Issues Tested

The security validation tests focused on input validation for benchmark-related functions.

| Function                 | Issue                         | Expected Fix       |
| ------------------------ | ----------------------------- | ------------------ |
| `make_data(n)`           | Negative size was accepted    | Raise `ValueError` |
| `make_data(n)`           | Non-integer size was accepted | Raise `TypeError`  |
| `run_benchmark(repeats)` | Zero repeats was accepted     | Raise `ValueError` |
| `run_benchmark(repeats)` | Negative repeats was accepted | Raise `ValueError` |

### Red Light Result

Before validation was added, the test failed because invalid input was not rejected.

```text
AssertionError: ValueError not raised
FAILED (failures=1, errors=2)
```

This confirmed that the Stage 5 security tests entered the expected red-light state.

### Green Light Result

After adding input validation to `benchmark.py`, the security tests passed.

```text
Ran 4 tests in 0.001s

OK
```

---

## Final Full Test

### Command

```bash
py -m unittest
```

### Result

```text
Ran 14 tests in 0.634s

OK
```

### Final Summary

All tests passed successfully.

| Test File          | Purpose                                  | Status |
| ------------------ | ---------------------------------------- | ------ |
| `test_sorts.py`    | Sorting correctness and input validation | Passed |
| `test_plot.py`     | Benchmark plot generation                | Passed |
| `test_security.py` | Security and input validation            | Passed |

Final status:

```text
OK
```
