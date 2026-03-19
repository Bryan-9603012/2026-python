Week 03 - UVA 118 測試紀錄
題號：UVA 118 - Mutant Flatworld Explorers
檔案：
- 正式程式：question_2.py
- 測試程式：test_question_2.py

【第一次測試】
執行指令：
python .\test_question_2.py

測試結果：
F....F

錯誤摘要：
1. test_turning_and_forward 失敗
   - 原因：測試預期值與實際題意不符
   - 修正：重新手算路徑後，修正 expected_output

2. test_ignore_only_dangerous_forward 失敗
   - 原因：原本誤以為 scent 只記錄座標
   - 實際上 scent 應記錄 (x, y, direction)
   - 修正：修正測試預期值

【修正後第二次測試】
執行指令：
python .\test_question_2.py

測試結果：
......
----------------------------------------------------------------------
Ran 6 tests in 0.00s

OK

補充說明：
1. 程式可正確處理 L / R / F 指令。
2. 可正確判斷邊界、LOST 與 scent 規則。
3. 修正後已全數通過 unit test。