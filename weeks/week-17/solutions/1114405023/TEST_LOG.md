# TEST_LOG.md

## Week 17 - 0617 timeit + 搜尋效能評估測試紀錄

---

## 一、紅燈測試紀錄

### 測試目的

先完成 `test_timing.py`，但尚未建立或尚未實作 `timing.py`，確認測試會先失敗，符合 TDD 的紅燈流程。

### 測試指令

```bash
python .\test_timing.py
```

### 實際結果

```text
Traceback (most recent call last):
  File "test_timing.py", line 8, in <module>
    from timing import timeit
ModuleNotFoundError: No module named 'timing'
```

### 結果判斷

測試失敗是預期結果，因為紅燈階段尚未建立 `timing.py`，所以 `from timing import timeit` 找不到模組。

紅燈階段完成後進行 commit：

```bash
git add .
git commit -m "test: add timing tests"
```

---

## 二、timeit 綠燈測試紀錄

### 測試目的

完成 `timing.py` 後，再次執行 `test_timing.py`，確認 `timeit` 裝飾器符合規格。

### 測試指令

```bash
python .\test_timing.py
```

### 實際結果

```text
.....
----------------------------------------------------------------------
Ran 5 tests in 0.002s

OK
```

### 結果判斷

`test_timing.py` 的 5 個測試全部通過，代表：

- 被裝飾函式的回傳值保持不變
- `repeat=1` 可以正常執行
- 預設 `repeat=3` 可以記錄三筆時間
- `repeat < 1` 會 raise ValueError
- 使用 `functools.wraps` 保留函式的 `__name__` 與 `__doc__`

綠燈階段完成後進行 commit：

```bash
git add .
git commit -m "feat: implement timing decorator"
```

---

## 三、search.py 測試紀錄

### 測試目的

確認 `linear_search` 與 `binary_search` 的功能正確，並確認兩者不會修改原始資料。

### 測試指令

```bash
python .\test_search.py
```

### 實際結果

```text
..........
----------------------------------------------------------------------
Ran 10 tests in 0.002s

OK
```

### 結果判斷

`test_search.py` 的 10 個測試全部通過，代表：

- `linear_search` 可以處理空 list
- `linear_search` 可以找到第一個元素
- `linear_search` 可以找到最後一個元素
- `linear_search` 找不到時會回傳 `-1`
- `binary_search` 可以處理空 list
- `binary_search` 可以找到第一個元素
- `binary_search` 可以找到最後一個元素
- `binary_search` 找不到時會回傳 `-1`
- `binary_search` 收到未排序資料時會 raise ValueError
- `linear_search` 與 `binary_search` 都不會修改原本的 data

---

## 四、搜尋效能評估紀錄

### 測試目的

使用自己完成的 `timeit` 裝飾器，比較 `linear_search` 與 `binary_search` 的執行時間。

### 測試設定

- 資料量：`100000`
- 目標值：`99999`
- `repeat=5`
- `linear_search`：從頭逐一搜尋到最後一個元素
- `binary_search`：使用二分搜尋，但會先檢查資料是否已排序

### 測試指令

```bash
python .\benchmark_search.py
```

### 實際結果

```text
linear_search result: 99999
linear_search records: [0.019753800006583333, 0.014262499986216426, 0.014361999987158924, 0.015371399998917291, 0.014716399949975312]
linear_search average: 0.015693219983950256

binary_search result: 99999
binary_search records: [0.01910969999153167, 0.019234399951528758, 0.020187899994198233, 0.019671699963510036, 0.03035640000598505]
binary_search average: 0.02171201998135075

linear / binary ratio: 0.7227894962066974
```

### 結果判斷

本次測試中，`linear_search` 平均約 `0.01569` 秒，`binary_search` 平均約 `0.02171` 秒，所以這次量測結果是 `linear_search` 較快。

原因是我的 `binary_search` 在搜尋前會先檢查資料是否已排序，這個檢查需要額外掃過整個 list，因此增加了成本。如果資料已經確定排序且要查詢很多次，`binary_search` 才會比較有優勢；如果只查一次，排序或檢查排序的成本可能不划算。

search 階段完成後進行 commit：

```bash
git add .
git commit -m "feat: add search functions and benchmark"
```

---

## 五、總結

本次練習完成：

- `test_timing.py`
- `timing.py`
- `search.py`
- `test_search.py`
- `benchmark_search.py`
- `README.md`
- `AI_LOG.md`
- `TEST_LOG.md`

測試結果：

```text
timeit 測試：Ran 5 tests OK
search 測試：Ran 10 tests OK
benchmark：成功輸出 linear_search 與 binary_search 的效能資料
```
