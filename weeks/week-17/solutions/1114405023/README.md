# Week 17 - 0617 timeit + 搜尋效能評估

## 今日目標

本次練習是 6/18 完整搜尋效能實驗的預演。  
目標是先用 TDD 完成 `timeit` 計時裝飾器，再用它比較 `linear_search` 與 `binary_search` 的搜尋效能。

---

## 任務一：timeit

本次完成 `timing.py`，提供 `timeit` 裝飾器。

### 功能說明

`timeit` 可以用來計算函式執行時間。

主要功能如下：

- 保持原函式回傳值不變
- 預設 `repeat=3`
- 每次呼叫會實際執行 `repeat` 次
- 每次耗時會記錄在 `records`
- 本次呼叫的平均耗時會記錄在 `last_elapsed`
- `repeat < 1` 時會 `raise ValueError`
- 使用 `functools.wraps` 保留原函式的 `__name__` 與 `__doc__`
- 裝飾器內不使用 `print`

---

## 任務一測試結果

### 紅燈階段

一開始先完成 `test_timing.py`，但尚未建立 `timing.py`，因此測試失敗。

錯誤結果：

```text
ModuleNotFoundError: No module named 'timing'
```

這符合 TDD 的紅燈流程，代表測試先被建立，而且能夠檢查尚未完成的實作。

### 綠燈階段

完成 `timing.py` 後，再次執行測試：

```bash
python .\test_timing.py
```

測試結果：

```text
Ran 5 tests in 0.002s

OK
```

代表 `timeit` 裝飾器符合本次規格。

---

## 任務二：搜尋效能評估

本次完成 `search.py`，其中包含兩個搜尋函式：

```python
linear_search(data, target)
binary_search(data, target)
```

### linear_search

`linear_search` 使用線性搜尋，從 list 第一個元素開始逐一比對。

- 找到目標值時回傳 index
- 找不到時回傳 `-1`
- 不會修改原本的 data

### binary_search

`binary_search` 使用二分搜尋。

- 前提是 data 必須已經由小到大排序
- 找到目標值時回傳 index
- 找不到時回傳 `-1`
- 不會修改原本的 data
- 如果 data 未排序，會 `raise ValueError`

---

## 搜尋功能測試結果

執行：

```bash
python .\test_search.py
```

結果：

```text
Ran 10 tests in 0.002s

OK
```

代表：

- `linear_search` 可以處理空 list
- `linear_search` 可以找到第一個元素
- `linear_search` 可以找到最後一個元素
- `linear_search` 找不到時會回傳 `-1`
- `binary_search` 可以處理空 list
- `binary_search` 可以找到第一個元素
- `binary_search` 可以找到最後一個元素
- `binary_search` 找不到時會回傳 `-1`
- `binary_search` 收到未排序資料時會 `raise ValueError`
- 兩個搜尋函式都不會修改原本的 data

---

## 搜尋效能測試設定

本次使用自己完成的 `timeit` 裝飾器進行測試。

測試設定：

- 資料量：`100000`
- 目標值：`99999`
- `repeat=5`
- `linear_search`：從頭搜尋到最後一個元素
- `binary_search`：使用二分搜尋，但會先檢查資料是否已排序

執行：

```bash
python .\benchmark_search.py
```

---

## 搜尋效能測試結果

```text
linear_search result: 99999
linear_search records: [0.019753800006583333, 0.014262499986216426, 0.014361999987158924, 0.015371399998917291, 0.014716399949975312]
linear_search average: 0.015693219983950256

binary_search result: 99999
binary_search records: [0.01910969999153167, 0.019234399951528758, 0.020187899994198233, 0.019671699963510036, 0.03035640000598505]
binary_search average: 0.02171201998135075

linear / binary ratio: 0.7227894962066974
```

---

## 搜尋效能評估

本次使用 `timeit` 比較 `linear_search` 與 `binary_search`，資料量為 `100000`，目標值放在最後一個位置。量測結果中，`linear_search` 平均約 `0.01569` 秒，`binary_search` 平均約 `0.02171` 秒，因此這次反而是 `linear_search` 較快。

原因是我的 `binary_search` 版本會先檢查資料是否已排序，這個檢查需要額外掃過整個 list，所以增加了成本。如果資料已經確定排序，且需要查詢很多次，`binary_search` 才會比較划算；但如果只查一次，排序或檢查排序的成本可能不值得。

---

## 本次學到的重點

1. TDD 要先寫測試，確認紅燈後再寫實作。
2. `raise ValueError` 適合用於正式輸入驗證，不能依賴 `assert`。
3. `functools.wraps` 可以保留原函式的 metadata。
4. `records` 可以記錄每次執行時間。
5. `last_elapsed` 可以記錄最近一次呼叫的平均耗時。
6. `binary_search` 的前提是資料必須已排序。
7. 效能不能只看理論時間複雜度，也要考慮排序或檢查排序的額外成本。

---

## 使用指令整理

### 執行 timeit 測試

```bash
python .\test_timing.py
```

### 執行搜尋測試

```bash
python .\test_search.py
```

### 執行搜尋效能評估

```bash
python .\benchmark_search.py
```

---

## Commit 紀錄

```bash
git commit -m "test: add timing tests"
git commit -m "feat: implement timing decorator"
git commit -m "feat: add search functions and benchmark"
git commit -m "docs: add logs and search evaluation"
```

本次流程符合先紅燈、再綠燈、最後補上搜尋評估與紀錄的順序。
