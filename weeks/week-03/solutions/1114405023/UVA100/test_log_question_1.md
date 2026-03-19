Week 03 - UVA 100 測試紀錄
題號：UVA 100 - The 3n + 1 Problem

檔案：
- 正式程式：question_1.py
- 測試程式：test_question_1.py

測試指令：
python .\test_question_1.py


【第一次測試】
問題描述：
一開始測試程式無法正常執行，出現模組與函式相關錯誤。

錯誤摘要：
1. ModuleNotFoundError: No module named 'uva100'
   原因：
   - 測試程式原本匯入的檔名與實際解答檔名不一致。

   修正方式：
   - 將測試程式中的 import 對應到正確檔名 question_1
   - 並確認檔名不使用減號（-），改用底線（_）

2. AttributeError: module 'question_1' has no attribute 'main'
   原因：
   - question_1.py 一開始沒有 main() 函式
   - 而測試程式是透過 question_1.main() 進行測試

   修正方式：
   - 將正式解題邏輯包進 main()
   - 並使用 if __name__ == "__main__": main() 結構

3. 題目範例測試失敗
   原因：
   - 程式一開始只處理單行輸入
   - 題目範例包含多組 i j，需要逐行讀取直到 EOF

   修正方式：
   - 改用 sys.stdin 逐行讀取輸入
   - 對每一組 i j 個別計算並輸出結果


【修正後第二次測試】
執行結果：
....
----------------------------------------------------------------------
Ran 4 tests in 0.00s

OK


【測試項目】
1. 題目範例測試
2. 單一數字區間測試
3. 反向區間測試
4. 小範圍區間測試


【結果說明】
1. 程式可正確處理一般區間輸入。
2. 程式可正確處理 i > j 的情況。
3. 程式可逐行讀取多組資料直到 EOF。
4. 程式輸出格式符合題目要求：i j max_cycle_length。
5. 修正後已通過所有 unit test。