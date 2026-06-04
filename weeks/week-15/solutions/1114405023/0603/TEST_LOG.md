# TEST_LOG.md

## 作業名稱

6/3 Starter — UVA 11417 GCD

## 測試目標

本次測試目標是確認 `sum_of_gcd(n)` 是否能正確計算：

```text
1 <= i < j <= n
```

範圍內所有 `gcd(i, j)` 的總和。

## 測試檔案

```text
test_gcd.py
```

## 被測試檔案

```text
gcd.py
```

## 測試案例

| 測試名稱               |       輸入 | 預期結果 | 說明                                   |
| ------------------ | -------: | ---: | ------------------------------------ |
| `test_n_equals_1`  |  `n = 1` |  `0` | 邊界案例，沒有任何 `i < j` 的組合                |
| `test_n_equals_2`  |  `n = 2` |  `1` | 只有 `gcd(1, 2) = 1`                   |
| `test_n_equals_10` | `n = 10` | `67` | UVA 11417 題目範例                       |
| `test_n_equals_3`  |  `n = 3` |  `3` | `gcd(1,2)+gcd(1,3)+gcd(2,3)=1+1+1=3` |

## 第一次測試：紅燈

### 執行指令

```bash
python .\test_gcd.py
```

### 測試結果

```text
ModuleNotFoundError: No module named 'gcd'
```

### 結果說明

第一次測試時，`test_gcd.py` 已經引用：

```python
from gcd import sum_of_gcd
```

但當時尚未建立 `gcd.py`，因此 Python 找不到 `gcd` 模組。

這代表測試已經開始檢查尚未實作的功能，符合 TDD 流程中的紅燈階段。

## 第二次測試：綠燈

### 執行指令

```bash
python .\test_gcd.py
```

### 測試結果

```text
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

### 結果說明

建立 `gcd.py` 並完成 `sum_of_gcd(n)` 後，再次執行測試，4 個測試案例全部通過。

## 結論

本次 TDD 流程完成以下階段：

1. 先撰寫 `test_gcd.py` 測試案例。
2. 執行測試並確認紅燈。
3. 建立 `gcd.py` 並實作 `sum_of_gcd(n)`。
4. 再次執行測試並確認綠燈。
5. 測試結果顯示 `OK`，代表目前實作符合測試案例預期。
