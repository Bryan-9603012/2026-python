# UVA 10908 — Largest Square 測試與實作紀錄

## 產出檔案

- `main.py`：直觀版主程式
- `main_optimized.py`：優化後主程式
- `test.py`：自動測試程式，會同時測 `main.py` 與 `main_optimized.py`
- `log.md`：本檔，記錄測試資料與執行結果

## 解題重點

原版逐層擴張檢查；優化版為每種字元建立 2D prefix sum，查詢時用二分搜尋半徑。

## 測試案例

共 2 組測試資料，包含題目範例與邊界測資。

## 執行方式

```bash
python3 test.py
```

## 測試結果

PASS

### stdout

```text
All tests passed.
```

### stderr

```text

```


## 追加檔案

- `main_optimized_clean.py`：無中文註解的簡化版主程式，邏輯與 `main_optimized.py` 相同。
- `test.py` 已同步加入此檔案測試。
