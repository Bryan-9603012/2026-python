# AI_LOG.md

## 作業名稱

6/4 Starter — 平方數計數

## 使用 AI 的目的

本次作業使用 AI 協助理解題目需求、設計 TDD 測試案例、確認紅燈與綠燈結果，以及整理 PR 所需的紀錄文件。

## 題目需求整理

本題需要實作 `count_squares(a, b)`，功能如下：

1. 回傳 `[a, b]` 區間內完全平方數的個數。
2. 區間包含端點 `a` 和 `b`。
3. 若 `a > b`，應丟出：

```python
ValueError("a must be <= b")
```

## 與 AI 討論的內容

### 1. 測試案例設計

AI 協助我設計至少 3 個測試案例，並確保包含題目要求的 edge case 與例外案例。

本次採用的測試案例包含：

| 測試名稱                           |                     輸入 |         預期結果 | 說明                     |
| ------------------------------ | ---------------------: | -----------: | ---------------------- |
| `test_basic_range`             | `count_squares(1, 10)` |          `3` | `[1, 10]` 中有 `1, 4, 9` |
| `test_single_point_square`     |  `count_squares(9, 9)` |          `1` | 單點區間，且該點是完全平方數         |
| `test_single_point_not_square` |  `count_squares(8, 8)` |          `0` | 單點區間，但該點不是完全平方數        |
| `test_invalid_input_raises`    |  `count_squares(5, 2)` | `ValueError` | `a > b` 時應丟出例外         |

### 2. TDD 紅燈確認

一開始先撰寫 `test_square_counter.py`，並加入：

```python
from square_counter import count_squares
```

在尚未建立 `square_counter.py` 的情況下執行測試，出現：

```text
ModuleNotFoundError: No module named 'square_counter'
```

AI 說明這代表測試已經開始檢查尚未實作的功能，符合 TDD 的紅燈階段。

### 3. TDD 綠燈確認

建立 `square_counter.py` 並完成 `count_squares(a, b)` 實作後，再次執行測試。

測試結果顯示：

```text
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

代表 4 個測試案例全部通過，符合 TDD 的綠燈階段。

## 我採用的 AI 建議

我採用了 AI 建議的測試案例設計，讓測試能覆蓋：

1. 一般區間。
2. 單點區間且為完全平方數。
3. 單點區間但不是完全平方數。
4. 錯誤輸入 `a > b` 的例外處理。

## 我自己完成的部分

1. 修改 `test_square_counter.py`，加入測試案例。
2. 執行測試並確認紅燈。
3. 建立 `square_counter.py`。
4. 實作 `count_squares(a, b)`。
5. 再次執行測試並確認綠燈。
6. 撰寫 `AI_LOG.md` 與 `TEST_LOG.md` 作為作業紀錄。

## 測試指令

```bash
python .\test_square_counter.py
```

或：

```bash
python -m unittest test_square_counter.py
```

## 測試結果

```text
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s

OK
```

## 心得

透過這次練習，我更熟悉 TDD 的流程。先寫測試可以先確認功能需求，再透過紅燈確認測試正在檢查尚未實作的功能。完成實作後，測試轉為綠燈，代表目前程式符合測試案例預期。
