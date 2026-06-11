## Project

6/11 Sort Lab — Sorting Algorithm Benchmark

## AI Collaboration Summary

本次作業使用 AI 協助完成排序效能實驗室的開發流程。開發過程依照 TDD 流程進行：

```text
Read spec → Dev for red(test commit) → Dev for green(feat commit) → push
```

主要完成內容包含：

1. 三種排序演算法測試與實作
2. Benchmark 時間量測
3. 加入 baseline 與加速排序方法
4. 產生效能折線圖
5. 安全性自掃與輸入驗證修補

---

## Stage 2 — Sorting Algorithms

### Prompt

```text
先幫我寫這三種排序的test.py再給我main.py(要加入時間計算)結果出來後再來想加速的方法
```

### AI Response Summary

AI 先依照作業規則要求走 TDD 流程，先提供 `test_sorts.py`，而不是直接給完整實作。測試內容包含三種排序方法：

```python
bubble_sort(data: list) -> list
quick_sort(data: list) -> list
merge_sort(data: list) -> list
```

測試案例包含：

1. 一般整數列表
2. 空列表
3. 單一元素列表
4. 已排序列表
5. 反向排序列表
6. 重複值列表
7. 負數列表
8. 不修改原始輸入 list
9. 非 list 輸入應丟出 `TypeError`

### Red Light

第一次執行測試時，因為尚未建立 `sorts.py`，所以出現紅燈：

```text
ModuleNotFoundError: No module named 'sorts'
```

### Green Light

建立 `sorts.py` 並實作三種排序後，測試通過：

```text
Ran 9 tests in 0.004s

OK
```

### What I Learned

這個階段讓我確認排序函式不應該修改原始資料，而是應該回傳新的 list。這樣可以保護原始資料，避免 benchmark 或其他流程被排序副作用影響。

---

## Stage 2 — Benchmark

### Prompt

```text
結果出來後再來想加速的方法
```

### AI Response Summary

AI 建議依照規格使用 `benchmark.py`，而不是只使用 `main.py`，因為作業規格中明確要求 `benchmark.py`。

`benchmark.py` 內容包含：

1. `make_data(n, seed=42)`：產生測試資料
2. `measure_time()`：計算排序平均耗時
3. `run_benchmark()`：執行多組 size 與 repeats 的 benchmark
4. `print_results_table()`：印出結果表格
5. `save_results()`：輸出 `results.json`

### Benchmark Result

第一次 benchmark 結果如下：

```text
Size      Bubble Sort       Quick Sort        Merge Sort
500       0.014721          0.000824          0.002033
1000      0.090232          0.001755          0.003436
2000      0.398714          0.003563          0.007574
4000      1.798110          0.008744          0.018010
```

### Observation

* `bubble_sort` 最慢，因為平均時間複雜度為 O(n²)。
* `quick_sort` 在本次資料中最快。
* `merge_sort` 表現穩定，但比 `quick_sort` 慢。

---

## Stage 3 — Baseline and Optimized Sorting

### Prompt

```text
only three method?
```

### AI Response Summary

AI 說明 Stage 2 只要求三種排序，但 Stage 3 需要加入：

1. Python 內建 `sorted()` 作為 baseline
2. 至少一種加速方案

因此最後 benchmark 中使用五種方法：

```python
bubble_sort
quick_sort
merge_sort
builtin_sorted
optimized_quick_sort
```

### Prompt

```text
ok
```

### AI Response Summary

AI 協助新增 Stage 3 紅燈測試，將 `builtin_sorted` 與 `optimized_quick_sort` 加入原本的排序正確性測試中。

### Red Light

因為 `sorts.py` 尚未實作新函式，因此測試失敗：

```text
ImportError: cannot import name 'builtin_sorted' from 'sorts'
```

### Green Light

加入以下兩個函式後測試通過：

```python
builtin_sorted(data: list) -> list
optimized_quick_sort(data: list) -> list
```

### Optimization Strategy

`optimized_quick_sort` 使用以下優化策略：

1. **median-of-three pivot**

   * 不固定取第一個元素當 pivot。
   * 使用 low、mid、high 三個位置的中位數作為 pivot。
   * 降低 quick sort 在特殊輸入下退化成 O(n²) 的機率。

2. **small-range insertion sort**

   * 當排序區間長度小於等於 16 時，改用 insertion sort。
   * 小資料量時 insertion sort 的常數成本較低，可以減少遞迴與 partition 的額外開銷。

3. **in-place partition**

   * 減少建立額外 list 的成本。
   * 相比原始 quick sort 使用 left、middle、right 三個暫存 list，optimized 版本能降低部分記憶體配置成本。

### Benchmark Result

加入 baseline 與 optimized quick sort 後，benchmark 結果如下：

```text
Size      bubble_sort              quick_sort               merge_sort              builtin_sorted           optimized_quick_sort
500       0.015886                 0.000830                 0.001907                0.000062                 0.001026
1000      0.082816                 0.001976                 0.003559                0.000097                 0.001452
2000      0.413051                 0.003571                 0.007382                0.000226                 0.003646
4000      1.717670                 0.007698                 0.017615                0.000625                 0.007525
```

### Speed Improvement

在 size = 4000 時：

```text
quick_sort:            0.007698 seconds
optimized_quick_sort:  0.007525 seconds
```

加速百分比：

```text
(0.007698 - 0.007525) / 0.007698 * 100 ≈ 2.25%
```

因此，在 size = 4000 時，`optimized_quick_sort` 相比原始 `quick_sort` 約加速 **2.25%**。

### Observation

`optimized_quick_sort` 在最大測資 size = 4000 時有小幅加速，但在部分較小測資中沒有穩定勝過原始 `quick_sort`。原因可能是資料量較小時，median-of-three、insertion sort 切換與額外函式呼叫成本會抵消優化收益。

整體最快的方法仍然是 Python 內建 `sorted()`，因為 Python 內建排序使用高度優化的 Timsort。

---

## Stage 4 — Plot Generation

### Prompt

```text
還需要產圖
```

### AI Response Summary

AI 說明 Stage 4 需要完成：

1. 讀取 `results.json`
2. 繪製折線圖
3. y 軸使用 log scale
4. 輸出 `assets/benchmark.png`
5. 在 `plot.py` 開頭使用 `matplotlib.use("Agg")`

### Red Light

先新增 `test_plot.py` 後，因為尚未建立 `plot.py`，測試失敗：

```text
ModuleNotFoundError: No module named 'plot'
```

### Green Light

建立 `plot.py` 後，測試可以成功產生圖片。

過程中曾遇到環境問題：

```text
ModuleNotFoundError: No module named 'matplotlib'
```

原因是 `python` 與 `py` 指向不同 Python 環境。最後使用 `py` 執行測試成功。

### Plot Test Result

```text
Ran 1 test in 0.909s

OK
```

### Generated File

```text
assets/benchmark.png
```

### Observation

圖表使用 log scale 作為 y 軸，可以清楚看出不同排序方法之間的效能差距。

圖表觀察：

1. `bubble_sort` 隨資料量增加，耗時上升最明顯。
2. `quick_sort` 與 `optimized_quick_sort` 的表現接近。
3. `merge_sort` 穩定成長，但本次測試中比 quick sort 慢。
4. `builtin_sorted` 明顯最快。

---

## Stage 5 — Security Self-Review

### Prompt

```text
ok
```

### AI Response Summary

AI 建議針對 benchmark 相關函式進行輸入驗證安全檢查，並新增 `test_security.py`。

### Security Issues Found

本次安全性自掃主要修補 **2 類問題，共 4 個測試案例**：

| Function                 | Problem        | Fix                                 |
| ------------------------ | -------------- | ----------------------------------- |
| `make_data(n)`           | 接受負數 size      | `n < 0` 時 raise `ValueError`        |
| `make_data(n)`           | 接受非整數 size     | 非 `int` 時 raise `TypeError`         |
| `run_benchmark(repeats)` | 接受 `repeats=0` | `repeats <= 0` 時 raise `ValueError` |
| `run_benchmark(repeats)` | 接受負數 repeats   | `repeats <= 0` 時 raise `ValueError` |

### Red Light

在尚未加入驗證前，測試失敗：

```text
AssertionError: ValueError not raised
FAILED (failures=1, errors=2)
```

這代表原本的程式沒有拒絕不合理輸入。

### Fix

在 `benchmark.py` 中加入輸入驗證：

```python
def make_data(n: int, seed: int = 42) -> list:
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    if n < 0:
        raise ValueError("n must be greater than or equal to 0")
```

以及：

```python
def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    if not isinstance(repeats, int):
        raise TypeError("repeats must be an integer")

    if repeats <= 0:
        raise ValueError("repeats must be greater than 0")
```

### Green Light

修正後，安全性測試通過：

```text
Ran 4 tests in 0.001s

OK
```

### OpenSSF Secure Coding Review Notes

本次依照 Python 安全程式原則進行檢查，重點如下：

1. **Input validation**

   * 已修補。
   * 對 `make_data(n)` 與 `run_benchmark(repeats)` 加入型別與範圍檢查。

2. **Avoid unsafe evaluation**

   * 不適用。
   * 程式沒有使用 `eval()` 或 `exec()`。

3. **Avoid shell injection**

   * 不適用。
   * 程式沒有使用 `subprocess` 或直接拼接 shell command。

4. **Use secure randomness for security-sensitive values**

   * 不適用。
   * `benchmark.py` 使用 `random.Random(seed)` 是為了產生可重現的 benchmark 測資，不是用於密碼、token 或安全敏感用途，因此不需要改用 `secrets`。

5. **File path handling**

   * 部分適用。
   * `plot.py` 會輸出 `assets/benchmark.png`，目前路徑固定且由程式控制，沒有接收不可信任使用者輸入，因此風險低。

### Number of Fixed Security Issues

本階段修補安全與穩定性問題共 **2 類**：

1. `make_data(n)` 缺少 size 輸入驗證
2. `run_benchmark(repeats)` 缺少 repeats 輸入驗證

對應測試案例共 **4 個**。

---

## Final Test

### Prompt

```text
幫我依照紀錄寫test_log.md
```

### Final Test Command

```bash
py -m unittest
```

### Final Test Result

```text
Ran 14 tests in 0.634s

OK
```

### Final Status

全部測試通過。

| Test File          | Purpose    | Result |
| ------------------ | ---------- | ------ |
| `test_sorts.py`    | 排序正確性與例外處理 | Passed |
| `test_plot.py`     | 圖片產生驗證     | Passed |
| `test_security.py` | 安全性與輸入驗證   | Passed |

---

## Reflection

本次作業讓我練習使用 TDD 流程完成排序演算法、效能測試、視覺化與安全性檢查。

最大的收穫是：

1. 測試應該先於實作，紅燈可以確認測試真的有檢查到需求。
2. 排序函式應避免修改原始輸入資料，降低副作用。
3. Benchmark 不只要看結果，也要保存 `results.json`，方便後續畫圖與比較。
4. 加速方法不一定在所有資料量都會變快，必須用實驗結果驗證。
5. 安全性檢查不只針對攻擊，也包含輸入驗證與避免不合理參數造成程式錯誤。
