# TEST_LOG.md

# 赤壁戰役 - 測試執行日誌

## Stage 1: 資料讀取與結構

### RED
- 先定義載入檔案、解析武將、EOF 結尾等測試需求。
- 初始狀態下，若未實作 `load_generals()`，測試會失敗。

### GREEN
- 完成 `load_generals()`
- 使用 `namedtuple` 建立 `General`
- 通過武將讀取、屬性解析、勢力分布與 EOF 測試

## Stage 2: 戰鬥模擬與統計

### GREEN
- 完成 `get_battle_order()`
- 完成 `calculate_damage()`
- 使用 `Counter` 統計傷害
- 使用 `defaultdict` 統計兵力損失
- 完成戰役模擬、傷害排名、勢力統計

## Stage 3: 重構與視覺化

### REFACTOR
- 加入 ASCII 戰役資訊輸出
- 加入 ASCII 傷害統計報表
- 確認邏輯功能不受影響


## 實際 unittest 輸出

```bash

```
