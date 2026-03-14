README.md
# Week 02 Python 作業

## 完成題目

- Task1 — Sequence Clean
- Task2 — Student Ranking
- Task3 — Log Summary

---

# 執行方式

Python 版本


Python 3.10+


執行程式：

Task1


python task1_sequence_clean.py


Task2


python task2_student_ranking.py


Task3


python task3_log_summary.py


執行測試：


python -m unittest discover -s tests -p "test_*.py" -v


---

# 資料結構選擇理由

### Task1

使用 `list` 儲存原始資料，  
並使用 `set` 記錄已出現過的元素來實作去重但保持順序。

### Task2

使用 `tuple` 儲存學生資料 `(name, score, age)`  
並使用 `sorted()` 搭配 `key` 來完成多條件排序。

### Task3

使用 `defaultdict` 統計每個 user 的事件數量，  
使用 `Counter` 統計 action 出現次數。

---

# 遇到的錯誤與修正

在 Task2 一開始排序 key 寫錯順序，  
導致同分數時排序不正確。  
後來改為：


key=lambda x: (-x[1], x[2], x[0])


才符合題目要求。

---

# Red → Green → Refactor

### Task1

Red：先寫測試，sequence_clean 尚未實作導致測試失敗。  
Green：實作 dedupe、排序與偶數篩選後測試通過。  
Refactor：將邏輯整理成函式並簡化程式結構。

### Task2

Red：測試排序規則時結果不正確。  
Green：修正 sorted key 的順序。  
Refactor：將排序邏輯抽成 student_ranking 函式。

### Task3

Red：初始版本沒有處理空輸入情況。  
Green：增加 `if action_counter:` 判斷。  
Refactor：將統計與排序邏輯整理為 log_summary 函式。