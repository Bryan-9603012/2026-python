# AI_USAGE.md

學生：1114405023 XXX

## 一、我問了哪些問題

1. 如何用 Python 讀取 UTF-8-BOM 的 CSV 檔案？
2. 如何把 CSV 資料過濾後輸出成 JSON？
3. 如何用 `xml.etree.ElementTree` 建立 XML 節點？
4. 如何用 unittest 寫 Task 1 與 Task 2 的測試？
5. 如何使用 matplotlib 畫出函式耗時比較圖？

## 二、AI 建議我有採用的部分

1. 讀取 CSV 時使用 `encoding="utf-8-sig"`，避免 BOM 造成欄位名稱錯誤。
2. 將功能拆成多個函式，例如 `read_csv()`、`filter_by_admission()`、`count_by_dept()`。
3. 使用 `pathlib.Path` 處理路徑，並在輸出前自動建立 `output/` 目錄。
4. XML 使用 `ElementTree` 建立，而不是用字串手動拼接，避免特殊字元造成 XML 格式錯誤。
5. 測試分成正常輸入、空輸入與錯誤格式三種情境。

## 三、AI 建議我拒絕的部分及原因

1. AI 曾建議直接把 `output/` 內的結果檔手動建立好，但我沒有採用，因為作業要求輸出資料應由程式產生。
2. AI 曾建議測試只寫 2 到 3 個案例，但我沒有採用，因為作業要求 Task 1 與 Task 2 各至少 5 個測試函式。
3. AI 曾建議圖表可以使用中文標題，但我依照作業最後的英文版規格，將圖表標題改成英文。

## 四、AI 輸出有誤的案例與修正過程

AI 一開始給的 CSV 讀取範例使用：

```python
open(filepath, encoding="utf-8")
```

實際檢查作業說明後，發現資料檔是 UTF-8-BOM。  
如果直接使用 `utf-8`，第一個欄位可能會包含 BOM 字元，導致欄位比對不穩定。

修正方式：

```python
open(filepath, encoding="utf-8-sig")
```

這樣可以正確處理 BOM，讓 `DictReader` 讀到乾淨的欄位名稱。
