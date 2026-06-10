AI 使用紀錄 1：閱讀 README 並整理需求
我實際輸入的提示詞
1.幫我閱讀README.md並簡短地告訴我需求
AI 回覆重點

AI 協助整理出這次作業需求：

需要先補 test_digit_root.py
至少要有 3 個 test case
測試要包含 edge case 與例外案例
之後建立 digit_root.py
函式名稱必須是 digit_root
n < 1 時要 raise ValueError("n must be >= 1")
最後使用 python -m unittest 確認測試通過
我採用的部分

我採用 AI 整理出的需求，確認這題應該先寫測試檔，再進行功能實作。

AI 使用紀錄 2：撰寫測試檔
我實際輸入的提示詞
幫我撰寫測試檔，並加入一個例外案例及一個edge case
AI 回覆重點

AI 建議使用 unittest 撰寫測試，並加入以下測試案例：

一位數直接回傳自己
多輪數字根案例
最大範圍附近的大數案例
最小合法輸入 1
n < 1 的例外案例
我採用的部分

我採用了 unittest.TestCase 的結構，並加入以下測試：

def test_single_digit_returns_itself(self):
    self.assertEqual(digit_root(7), 7)

def test_multiple_rounds_digit_root(self):
    self.assertEqual(digit_root(199), 1)

def test_large_number(self):
    self.assertEqual(digit_root(2000000000), 2)

def test_edge_case_minimum_valid_number(self):
    self.assertEqual(digit_root(1), 1)

def test_raises_value_error_when_less_than_one(self):
    with self.assertRaisesRegex(ValueError, "n must be >= 1"):
        digit_root(0)
AI 使用紀錄 3：除錯非整數輸入測試
我實際輸入的提示詞
File "C:\Users\10801\OneDrive\เอกสาร\資料夾\2026-python\weeks\week-16\solutions\1114405023\0610\test_digit_root.py", line 25, in test_raises_value_error_when_not_an_integer
    digit_root("not an integer")
  File "C:\Users\10801\OneDrive\เอกสาร\資料夾\2026-python\weeks\week-16\solutions\1114405023\0610\digit_root.py", line 2, in digit_root
    if n < 1:
       ^^^^^
TypeError: '<' not supported between instances of 'str' and 'int'

----------------------------------------------------------------------  
Ran 6 tests in 0.007s

FAILED (errors=1)
AI 回覆重點

AI 說明錯誤原因是我傳入了字串：

digit_root("not an integer")

但 digit_root.py 內部會先做：

if n < 1:

字串無法和整數比較，所以會出現 TypeError。

AI 也提醒 README 只要求處理 n < 1，沒有要求處理非整數輸入。

我採用的部分

我決定不測試字串輸入，改成測試題目有要求的 n < 1 例外情況。

AI 使用紀錄 4：修正例外案例
我實際輸入的提示詞
[貼上測試結果截圖，顯示 test_raises_value_error_when_not_an_integer 失敗，錯誤為 AssertionError: ValueError not raised]
AI 回覆重點

AI 指出這個測試名稱和測試內容不一致。

當時測試名稱是：

test_raises_value_error_when_not_an_integer

但實際測試內容已經改成：

digit_root(-1)

因此這不是「not an integer」案例，而是「negative number」案例。

我採用的部分

我保留負數測試，因為 -1 符合 README 中 n < 1 必須 raise ValueError 的需求。
最後測試可以正常通過。

最終測試結果

執行指令：

python -m unittest -v test_digit_root.py

結果：

test_edge_case_minimum_valid_number ... ok
test_large_number ... ok
test_multiple_rounds_digit_root ... ok
test_raises_value_error_when_less_than_one ... ok
test_raises_value_error_when_not_an_integer ... ok
test_single_digit_returns_itself ... ok

Ran 6 tests in 0.002s

OK