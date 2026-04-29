# 10242 log

## 正式版 main.py
- 使用 Kosaraju 找強連通分量 SCC。
- SCC 內節點可互相走到，因此現金可合併。
- SCC 壓縮成 DAG 後，用 DFS memo 找到任一酒吧的最大金額。

## 優化簡化版 main_simple.py
- 保留 SCC + DAG DP 的核心最佳解法。
- 程式比正式版短，適合交作業與快速理解。

## 差異比較
| 項目 | main.py | main_simple.py |
|---|---|---|
| 演算法 | SCC + DAG DP | SCC + DAG DP |
| DP 寫法 | DFS memo | DFS memo |
| 時間 | O(N+M) | O(N+M) |
| 記憶體 | O(N+M) | O(N+M) |

## 測試
```bash
python3 test.py
```
