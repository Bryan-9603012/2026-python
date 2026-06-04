# TEST_LOG.md

## 作業名稱

6/4 Starter — 平方數計數

## 測試目標

本次測試目標是確認 `count_squares(a, b)` 是否能正確計算 `[a, b]` 區間內完全平方數的個數，並確認錯誤輸入時會正確丟出例外。

## 測試檔案

```text
test_square_counter.py
```

## 被測試檔案

```text
square_counter.py
```

## 測試案例

| 測試名稱                           |                     輸入 |         預期結果 | 說明                           |
| ------------------------------ | ---------------------: | -----------: | ---------------------------- |
| `test_basic_range`             | `count_squares(1, 10)` |          `3` | `[1, 10]` 裡的完全平方數是 `1, 4, 9` |
| `test_single_point_square`     |  `count_squares(9, 9)` |          `1` | 單點區間，且 `9` 是完全平方數            |
| `test_single_point_not_square` |  `count_squares(8, 8)` |          `0` | 單點區間，但 `8` 不是完全平方數           |
| `test_invalid_input_raises`    |  `count_squares(5, 2)` | `ValueError` | `a > b` 時應丟出例外               |

## 第一次測試：紅燈

### 執行指令

```bash
python .\test_square_counter.py
```

### 測試結果

```text
Traceback (most recent call last):
  File "...\test_square_counter.py", line 9, in <module>
    from square_counter import count_squares
ModuleNotFoundError: No module named 'square_counter'
```

### 結果說明

第一次測試時，`test_square_counter.py` 已經引用：

```python
from square_counter import count_squares
```

但當時尚未建立 `square_counter.py`，因此 Python 找不到 `square_counter` 模組。

這代表測試已經開始檢查尚未實作的功能，符合 TDD 流程中的紅燈階段。

## 第二次測試：綠燈

### 執行指令

```bash
python .\test_square_counter.py
```

### 測試結果

```text
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

### 結果說明

建立 `square_counter.py` 並完成 `count_squares(a, b)` 實作後，再次執行測試，4 個測試案例全部通過。

## 結論

本次 TDD 流程完成以下階段：

1. 先撰寫 `test_square_counter.py` 測試案例。
2. 執行測試並確認紅燈。
3. 建立 `square_counter.py` 並實作 `count_squares(a, b)`。
4. 再次執行測試並確認綠燈。
5. 測試結果顯示 `OK`，代表目前實作符合測試案例預期。
