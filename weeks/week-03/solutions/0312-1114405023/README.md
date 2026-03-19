# Week 03 - Robot Lost
學號：0312-1114405023

## 專案簡介
這個作業是將 UVA 118「Robot Lost」題目的核心規則，實作成一個可測試的 Python 模組，並額外使用 `pygame` 製作互動式視覺化遊戲介面。

專案分成兩個主要部分：

- `robot_core.py`：負責機器人移動、轉向、越界判斷、LOST 狀態、scent 規則
- `robot_game.py`：負責 pygame 畫面顯示、鍵盤控制、機器人與 scent 的視覺化

---

## 功能清單

### 核心規則功能
- 支援機器人方向 `N / E / S / W`
- 支援指令：
  - `L`：左轉
  - `R`：右轉
  - `F`：前進一格
- 若前進後超出地圖範圍，機器人會變成 `LOST`
- 機器人掉出地圖前，會在原位置與方向留下 `scent`
- 若其他機器人在相同位置、相同方向再次執行危險 `F`，則會忽略這次指令，不會掉出去
- 支援格式化輸出結果

### 遊戲功能
- 顯示格子地圖
- 顯示機器人位置
- 顯示機器人朝向
- 顯示 scent 標記
- 支援鍵盤互動操作
- 可建立新機器人
- 可清除 scent

---

## 檔案結構

```text
0312-1114405023-homework/
├── robot_core.py
├── robot_game.py
├── tests/
│   ├── test_robot_core.py
│   └── test_robot_scent.py
├── assets/
│   └── gameplay.png
├── README.md
├── TEST_CASES.md
├── TEST_LOG.md
└── AI_USAGE.md

執行方式
1. 執行核心規則版本

可以使用標準輸入格式執行：

python .\robot_core.py

也可以搭配輸入檔：

python .\robot_core.py < input.txt
範例輸入
5 3
1 1 E
RFRFRFRF
3 2 N
FRRFLLFFRRFLL
0 3 W
LLFFFLFLFL
範例輸出
1 1 E
3 3 N LOST
2 3 S
遊戲執行方式

先安裝 pygame：

py -m pip install pygame

再執行：

py .\robot_game.py
遊戲操作方式

L：左轉

R：右轉

F：前進

N：建立新機器人（重設到 (0, 0, N)）

C：清除所有 scent

ESC：離開遊戲

測試方式
執行單一測試檔
python .\tests\test_robot_core.py
python .\tests\test_robot_scent.py

