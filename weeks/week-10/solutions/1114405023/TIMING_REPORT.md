# TIMING_REPORT.md

學生：1114405023 XXX

## 執行結果

以下為一次執行 Task 1 與 Task 2 後記錄的 `@timeit` 輸出。  
實際秒數會依照電腦效能、資料筆數與當下系統負載不同而變化。

```text
[timeit] read_csv 耗時 0.002341s
[timeit] write_json 耗時 0.001203s
[timeit] read_json 耗時 0.000891s
[timeit] write_xml 耗時 0.003412s
```

## 問題回答

### 1. 哪個操作最耗時？你認為原因是什麼？

這次紀錄中最耗時的是 `write_xml`。  
原因是 XML 輸出不只是單純把資料寫入檔案，還需要先建立 ElementTree 結構，將每一筆學生資料轉成 `<student>` 節點，最後再產生 XML 宣告與檔案內容。

### 2. read_csv 比 read_json 快還是慢？與課堂 U01 的比較實驗結果一致嗎？

這次紀錄中 `read_csv` 比 `read_json` 慢。  
原因是 CSV 需要逐列讀取，並透過欄位名稱組成 `dict`；JSON 則可以直接由 `json.load()` 解析成 Python 的 dict/list 結構。  
這與一般資料格式比較的結果大致一致：JSON 在結構化資料讀取上通常較方便，而 CSV 需要額外處理欄位與列資料。

### 3. write_xml 比 write_json 快還是慢？原因為何？

這次紀錄中 `write_xml` 比 `write_json` 慢。  
原因是 JSON 可以直接用 `json.dump()` 將 dict/list 輸出，而 XML 需要建立節點、設定屬性、處理縮排與 XML 宣告，所以步驟較多。

### 4. 如果資料筆數從 100 增加到 10000，你預期各函式耗時如何變化？

我預期四個函式的耗時都會增加，而且大致會隨資料筆數呈現線性成長。  
`read_csv` 和 `read_json` 會因為讀取資料量增加而變慢；`write_json` 和 `write_xml` 會因為輸出內容變多而變慢。  
其中 `write_xml` 可能增加得更明顯，因為每一筆資料都要建立一個 XML 節點。
