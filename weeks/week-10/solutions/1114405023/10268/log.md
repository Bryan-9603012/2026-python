# 10268 log

## 正式版 main.py
- 使用反向蛋掉落 DP。
- `dp[e]` 表示目前 t 次測試、e 顆球最多可測幾層。
- 轉移：`dp[e] = dp[e] + dp[e-1] + 1`。

## 優化簡化版 main_simple.py
- 使用一維 DP，不建立二維表。
- 從 1 到 63 次測試找第一個可覆蓋 n 層的答案。

## 差異比較
| 項目 | main.py | main_simple.py |
|---|---|---|
| 演算法 | 一維 Egg Dropping DP | 一維 Egg Dropping DP |
| 時間 | O(63K) | O(63K) |
| 記憶體 | O(K) | O(K) |

## 測試
```bash
python3 test.py
```
