# Week 10 作業：資料格式轉換

學生：1114405023 XXX

## 一、完成項目

本作業完成以下三個任務：

1. Task 1：讀取 Week 08 的 NPU 新生資料 CSV，篩選 `入學方式 == 聯合登記分發`，統計各系所人數，輸出 `output/students.json`
2. Task 2：讀取 `output/students.json`，轉換為 XML 格式，輸出 `output/students.xml`
3. Task 3：讀取 `TIMING_REPORT.md` 的 timeit 結果，繪製函式耗時比較圖 `output/timing_comparison.png`

另外也完成：

- `tests/test_task1.py`
- `tests/test_task2.py`
- `TEST_LOG.md`
- `TIMING_REPORT.md`
- `AI_USAGE.md`

## 二、檔案結構

```text
weeks/week-10/solutions/1114405023/
├── task1_csv_to_json.py
├── task2_json_to_xml.py
├── task3_plot_comparison.py
├── output/
│   ├── students.json
│   ├── students.xml
│   └── timing_comparison.png
├── tests/
│   ├── test_task1.py
│   └── test_task2.py
├── TIMING_REPORT.md
├── TEST_LOG.md
├── AI_USAGE.md
└── README.md
```

## 三、執行方式

請先確認目前工作目錄在：

```bash
weeks/week-10/solutions/1114405023/
```

執行 Task 1：

```bash
python task1_csv_to_json.py
```

執行 Task 2：

```bash
python task2_json_to_xml.py
```

執行 Task 3：

```bash
python task3_plot_comparison.py
```

執行全部測試：

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## 四、@timeit 裝飾器說明

`@timeit` 是一個裝飾器，它會把原本的函式包在 `wrapper()` 裡面。  
當函式被呼叫時，`wrapper()` 會先記錄開始時間，等原函式執行完後再記錄結束時間，兩者相減就能得到函式耗時。  
我在 `read_csv()`、`write_json()`、`read_json()`、`write_xml()` 都套用了這個裝飾器，用來比較不同資料格式讀寫的效能。

## 五、遇到的 bug 與修正方式

我一開始在讀取 CSV 時使用：

```python
encoding="utf-8"
```

但作業說明提到 CSV 是 UTF-8-BOM，因此欄位名稱可能會出現隱藏的 BOM 字元，導致 `row.get("入學方式")` 找不到正確欄位。  
修正方式是將讀取編碼改成：

```python
encoding="utf-8-sig"
```

這樣 Python 會自動處理 BOM，欄位名稱就能正常對應。
