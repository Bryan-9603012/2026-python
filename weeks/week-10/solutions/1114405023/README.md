# UVA / ZeroJudge 作業程式包

包含 10226、10235、10242、10252、10268 五題。

每題都有：
- `main.py`：正式版。
- `main_simple.py`：優化後簡化版。
- `test.py`：基本測試。
- `log.md`：演算法、優化點、正式版與簡化版差異比較。

## 執行
```bash
cd 10268
python3 main.py < input.txt
python3 test.py
```

## 摘要
| 題號 | 方法 |
|---|---|
| 10226 | DFS + 剪枝 + 差異後綴輸出 |
| 10235 | Profile DP / 輪廓線 DP |
| 10242 | SCC 壓縮 + DAG DP |
| 10252 | 中位數最小化 Manhattan distance |
| 10268 | Egg Dropping 一維 DP |
