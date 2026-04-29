# 10235 log

## 正式版 main.py
- 使用 profile DP / 輪廓線 DP。
- 每個可用格必須剛好有 2 條選中邊，代表蛇身通過。
- 插座格不可有任何邊進出。

## 優化簡化版 main_simple.py
- 簡化版仍使用 profile DP，沒有改成慢速暴力搜尋。
- 狀態是 `(mask, left)`：mask 表示上方連線，left 表示左方連線。

## 差異比較
| 項目 | main.py | main_simple.py |
|---|---|---|
| 演算法 | Profile DP | Profile DP |
| 是否暴力 | 否 | 否 |
| 時間 | 約 O(N*M*狀態數*4) | 同左 |
| 記憶體 | O(2^M) | O(2^M) |

## 測試
```bash
python3 test.py
```
