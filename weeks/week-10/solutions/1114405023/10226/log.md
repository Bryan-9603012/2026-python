# 10226 log

## 正式版 main.py
- 多筆測資直到 EOF。
- DFS 依 A, B, C... 順序嘗試，因此自然符合字典序。
- 使用 `used` 與 forbidden position 直接剪枝。

## 優化簡化版 main_simple.py
- 不是暴力 `itertools.permutations` 後再過濾。
- 保留 DFS 剪枝，只把變數與流程縮短。

## 差異比較
| 項目 | main.py | main_simple.py |
|---|---|---|
| 可讀性 | 註解與結構較完整 | 更短，適合考場 |
| 演算法 | DFS + 剪枝 | DFS + 剪枝 |
| 時間 | 最壞 O(N!) | 最壞 O(N!) |
| 記憶體 | O(N) | O(N) |

## 測試
```bash
python3 test.py
```
