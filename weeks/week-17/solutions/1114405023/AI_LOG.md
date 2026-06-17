# AI_LOG.md

## Week 17 - 0617 AI 協作紀錄

## 使用 AI 的目的

本次使用 AI 協助完成 Week 17 0617 預演練習。練習內容包含：

- 使用 TDD 完成 `timeit` 計時裝飾器
- 撰寫 `test_timing.py`
- 完成 `timing.py`
- 撰寫 `linear_search` 與 `binary_search`
- 撰寫搜尋測試
- 使用自己的 `timeit` 比較搜尋效能
- 整理 `README.md`、`TEST_LOG.md` 與 `AI_LOG.md`

---

## AI 反問我什麼 / 我怎麼回答

| AI 反問內容 | 我的回答 | 檢查狀態 |
|---|---|---|
| `timeit` 的函式簽名與回傳型別是什麼？ | 被裝飾的函式回傳 `int`，`timeit` 要保持原本回傳值不變 | ✅ |
| `repeat` 的輸入範圍／邊界條件是什麼？ | `repeat` 必須是大於等於 `1` 的 `int` | ✅ |
| `repeat < 1` 時要怎麼處理？ | `raise ValueError` | ✅ |
| `timeit` 的 edge case 要測什麼？ | 測 `repeat = 1` | ✅ |
| 什麼情況算紅燈？ | `test_timing.py` 已經寫好，但 `timing.py` 尚未建立或尚未實作，所以測試失敗 | ✅ |
| 實作檔案名稱是 `main.py` 嗎？ | 不是，依照本次規格應該是 `timing.py` | ✅ |
| 為什麼 `repeat < 1` 要用 `raise ValueError`，不能用 `assert`？ | 因為 `assert` 可能在最佳化模式被停用，導致檢查失效；正式輸入驗證應該使用 `raise ValueError` | ✅ |
| `linear_search` / `binary_search` 找到與找不到時要回傳什麼？ | 找到回傳 `index`，找不到回傳 `-1` | ✅ |
| `data` 可以是空 list 嗎？ | 可以，找不到就回傳 `-1` | ✅ |
| `binary_search` 遇到未排序資料時要怎麼處理？ | 要 `raise ValueError` | ✅ |
| 搜尋的 edge case 要測什麼？ | 空 list、找第一個、找最後一個、找不到 | ✅ |
| 什麼情況算 `search.py` 完成？ | 兩個搜尋都正確、不修改原資料、可以用 `timeit` 測速度 | ✅ |
| `binary_search` 為什麼一定要求資料已排序？ | 因為它每次靠中間值判斷要往左還是往右找 | ✅ |

---

## 我改了什麼

### 紅燈階段

先建立 `test_timing.py`，測試 `timeit` 裝飾器應該具備的功能：

- 保持原函式回傳值不變
- `repeat=1` 時只記錄一筆時間
- 預設 `repeat=3` 時記錄三筆時間
- `repeat < 1` 時 raise ValueError
- 使用 `functools.wraps` 保留 `__name__` 與 `__doc__`

此時尚未建立 `timing.py`，所以測試出現：

```text
ModuleNotFoundError: No module named 'timing'
```

這代表紅燈成功。

---

### 綠燈階段

建立 `timing.py`，完成 `timeit` 裝飾器。

主要功能：

- 使用 `perf_counter()` 計算時間
- 使用 `repeat` 控制每次呼叫要重複執行幾次
- 每次耗時 append 到 `records`
- 本次平均耗時存到 `last_elapsed`
- 回傳原函式最後一次執行的結果
- `repeat < 1` 時使用 `raise ValueError`
- 使用 `functools.wraps` 保留函式 metadata

完成後重新執行 `test_timing.py`，測試全部通過。

---

### 搜尋階段

建立 `search.py`，完成：

- `linear_search(data, target)`
- `binary_search(data, target)`

`linear_search` 使用逐一比對，找到回傳 index，找不到回傳 `-1`。

`binary_search` 使用二分搜尋，前提是資料必須已排序。若收到未排序資料，會 `raise ValueError`。

另外建立 `test_search.py` 測試：

- 空 list
- 找第一個元素
- 找最後一個元素
- 找不到資料
- 未排序資料丟給 `binary_search`
- 確認搜尋函式不會修改原本的 data

最後建立 `benchmark_search.py`，使用自己的 `timeit` 比較 `linear_search` 與 `binary_search` 的速度。

---

## 我怎麼驗收

### timeit 紅燈驗收

執行：

```bash
python .\test_timing.py
```

結果：

```text
ModuleNotFoundError: No module named 'timing'
```

因為測試檔已存在但實作檔尚未建立，所以紅燈成立。

---

### timeit 綠燈驗收

執行：

```bash
python .\test_timing.py
```

結果：

```text
.....
----------------------------------------------------------------------
Ran 5 tests in 0.002s

OK
```

代表 `timeit` 測試全部通過。

---

### search.py 驗收

執行：

```bash
python .\test_search.py
```

結果：

```text
..........
----------------------------------------------------------------------
Ran 10 tests in 0.002s

OK
```

代表 `linear_search` 與 `binary_search` 的功能測試全部通過。

---

### 搜尋效能驗收

執行：

```bash
python .\benchmark_search.py
```

結果：

```text
linear_search result: 99999
linear_search records: [0.019753800006583333, 0.014262499986216426, 0.014361999987158924, 0.015371399998917291, 0.014716399949975312]
linear_search average: 0.015693219983950256

binary_search result: 99999
binary_search records: [0.01910969999153167, 0.019234399951528758, 0.020187899994198233, 0.019671699963510036, 0.03035640000598505]
binary_search average: 0.02171201998135075

linear / binary ratio: 0.7227894962066974
```

本次結果顯示 `linear_search` 比 `binary_search` 快。原因是 `binary_search` 在搜尋前會先檢查資料是否已排序，而這個檢查本身需要掃過整個 list，所以增加了額外成本。

---

## 遇到的問題與解決方式

| 問題 | 原因 | 解決方式 |
|---|---|---|
| `ModuleNotFoundError: No module named 'timing'` | 紅燈階段尚未建立 `timing.py` | 這是預期結果，先 commit 紅燈 |
| 一開始把實作檔想成 `main.py` | 本次教案規格指定檔案是 `timing.py` | 改用正確檔名 `timing.py` |
| `binary_search` 沒有比 `linear_search` 快 | `binary_search` 先檢查資料是否排序，額外增加掃描成本 | 在 README 中說明：如果資料已排序且查詢很多次，binary search 才較划算 |
| 需要記錄 AI 問答 | 本週 AI_LOG 要新增「AI 反問我什麼 / 我怎麼回答」欄 | 將 AI 的問題與我的回答整理成表格 |

---

## 本次學到的重點

1. TDD 要先寫測試，確認紅燈後再寫實作。
2. `raise ValueError` 適合用於正式的輸入驗證，不能依賴 `assert`。
3. `functools.wraps` 可以保留原函式的 metadata。
4. `records` 可以保存每次實際執行的耗時紀錄。
5. `last_elapsed` 可以保存最近一次呼叫的平均耗時。
6. `binary_search` 的前提是資料必須已排序。
7. 理論上的時間複雜度不一定等於實際測量結果，因為額外檢查或排序成本也會影響效能。
8. 如果只查一次，排序或檢查排序可能不划算；如果已排序且要查很多次，`binary_search` 才比較有優勢。

---

## Commit 紀錄

本次練習的 commit 順序如下：

```bash
git commit -m "test: add timing tests"
git commit -m "feat: implement timing decorator"
git commit -m "feat: add search functions and benchmark"
git commit -m "docs: add logs and search evaluation"
```

重點是先完成紅燈 `test:` commit，再完成綠燈 `feat:` commit。
