# 10252 log

## 正式版 main.py
- 將 x、y 分開處理。
- Manhattan 距離的最小和由中位數決定。
- 偶數個點時，中位數區間內所有整數都能達到同樣最小值。

## 優化簡化版 main_simple.py
- 不枚舉座標平面。
- 排序後直接計算中位數區間與最小距離和。

## 差異比較
| 項目 | main.py | main_simple.py |
|---|---|---|
| 演算法 | 中位數 | 中位數 |
| 時間 | O(N log N) | O(N log N) |
| 記憶體 | O(N) | O(N) |

## 測試
```bash
python3 test.py
```
