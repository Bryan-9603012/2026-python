# TEST LOG

## 測試環境
- 作業系統：Windows
- Python 版本：Python 3.13
- 測試框架：unittest

---

## 第一次測試（Red）
### 執行指令
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

測試結果

Total: 20
Passed: 10
Failed: 10

問題描述
一開始只完成了 turn_left() 與 turn_right() 的邏輯，因此 test_robot_core.py 可以通過，但 test_robot_scent.py 相關的測試尚未完成。

當時的問題包含：
F 指令處理不完整
scent 邏輯尚未正確加入
越界後沒有正確標記 LOST
LOST 後沒有停止後續指令
非法指令處理尚未完成

修改內容

補上 move_forward()
補上 is_out_of_bounds()
補上 execute_command()
補上 execute_commands()
加入 scent 檢查與 LOST 邏輯
加入非法指令 ValueError 處理

## 第二次測試（Green）
### 執行指令
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

測試結果
Total: 20
Passed: 20
Failed: 0

結果說明
在補上核心規則後，兩份測試檔全部通過：
test_robot_core.py
test_robot_scent.py
代表目前已正確完成：
左右轉
前進
邊界判斷
LOST
scent
同位置不同方向區分
LOST 後停止
非法指令錯誤處理

## Refactor 階段

重構內容

在測試全綠後，進一步把程式整理成較清楚的模組化設計：
建立 Robot 類別集中管理狀態
將前進邏輯抽成 move_forward()
將越界判斷抽成 is_out_of_bounds()
將單一步驟抽成 execute_command()
將多步指令抽成 execute_commands()
將輸出格式抽成 format_robot_output()

重構後效果
程式可讀性更好
更方便寫測試
更容易讓 robot_game.py 重用核心邏輯
符合作業要求的「邏輯層與畫面層分離」