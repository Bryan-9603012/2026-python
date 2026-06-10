# TEST_LOG.md

## 測試日期

2026-06-10

## 題目

6/10 數字根（Digit Root）

## 測試目標

確認 `digit_root(n: int) -> int` 是否符合題目規格：

1. 能將多位數反覆加總各位數，直到只剩一位數。
2. 一位數輸入應直接回傳自己。
3. 大數輸入仍能正確計算。
4. `n < 1` 時必須丟出 `ValueError("n must be >= 1")`。

## 測試檔案

```text
test_digit_root.py
```

## 被測試檔案

```text
digit_root.py
```

## 測試案例

| 測試名稱                                    |              輸入 |                                 預期結果 | 測試目的                    |
| --------------------------------------- | --------------: | -----------------------------------: | ----------------------- |
| `test_multi_digit_number`               |           `199` |                                  `1` | 測試多位數需要反覆加總的基本案例        |
| `test_single_digit_number`              |             `5` |                                  `5` | 測試一位數 edge case，應直接回傳自己 |
| `test_large_number`                     | `2_000_000_000` |                                  `2` | 測試大數 edge case          |
| `test_invalid_input_raises_value_error` |             `0` | raise `ValueError("n must be >= 1")` | 測試非法輸入與錯誤訊息             |

## Red 階段紀錄

先建立 `test_digit_root.py`，尚未建立 `digit_root.py`。

執行指令：

```bash
python -m unittest
```

測試結果：

```text
ModuleNotFoundError: No module named 'digit_root'
```

判斷：

這是預期中的紅燈，因為測試已經開始檢查 `digit_root` 函式，但實作檔案尚未建立。

紅燈 commit：

```bash
git add test_digit_root.py
git commit -m "test: add digit root tests"
```

## Green 階段紀錄

建立 `digit_root.py` 並完成 `digit_root()` 實作。

執行指令：

```bash
python -m unittest
```

測試結果：

```text
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

判斷：

所有測試通過，代表 `digit_root()` 已符合目前測試案例與題目要求。

綠燈 commit：

```bash
git add digit_root.py
git commit -m "feat: implement digit root"
```

## 測試結論

本次測試共設計 4 個 test case，已涵蓋：

* 基本多位數案例
* 一位數 edge case
* 大數 edge case
* 非法輸入例外案例

最後執行 `python -m unittest`，測試結果全部通過。
