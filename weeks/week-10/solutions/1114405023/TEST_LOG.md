# TEST_LOG.md

學生：1114405023 XXX

## Task 1

### Red（失敗紀錄）

執行指令：

```bash
python -m unittest tests/test_task1.py -v
```

結果：

```text
ERROR: test_filter_keeps_correct_rows
ImportError: cannot import name 'filter_by_admission' from 'task1_csv_to_json'

Ran 1 test in 0.001s

FAILED (errors=1)
```

失敗原因：

`tests/test_task1.py` 已先寫好測試，但 `task1_csv_to_json.py` 尚未實作 `filter_by_admission()`，所以測試在 import 階段失敗。

### Green（通過紀錄）

執行指令：

```bash
python -m unittest tests/test_task1.py -v
```

結果：

```text
test_filter_keeps_correct_rows ... ok
test_filter_removes_others ... ok
test_filter_empty_input ... ok
test_count_by_dept_correct ... ok
test_count_by_dept_empty ... ok

Ran 5 tests in 0.002s

OK
```

讓測試通過的關鍵修改：

- 實作 `filter_by_admission(rows, method)`
- 使用 list comprehension 過濾 `入學方式`
- 實作 `count_by_dept(rows)` 統計各系所人數

### Refactor（重構紀錄）

執行指令：

```bash
python -m unittest tests/test_task1.py -v
```

結果：

```text
test_build_output_data_format ... ok
test_count_by_dept_correct ... ok
test_count_by_dept_empty ... ok
test_filter_empty_input ... ok
test_filter_keeps_correct_rows ... ok
test_filter_removes_others ... ok
test_read_csv_and_write_json ... ok

Ran 7 tests in 0.006s

OK
```

重構內容：

- 補上型別提示
- 新增 `build_output_data()` 統一整理 JSON 輸出格式
- `read_csv()` 使用 `encoding="utf-8-sig"` 避免 BOM 問題
- `write_json()` 自動建立 `output/` 目錄

---

## Task 2

### Red（失敗紀錄）

執行指令：

```bash
python -m unittest tests/test_task2.py -v
```

結果：

```text
ERROR: test_root_tag_and_attrs
ImportError: cannot import name 'build_xml_tree' from 'task2_json_to_xml'

Ran 1 test in 0.001s

FAILED (errors=1)
```

失敗原因：

`tests/test_task2.py` 已先寫好 XML 結構測試，但 `task2_json_to_xml.py` 尚未實作 `build_xml_tree()`，因此 import 失敗。

### Green（通過紀錄）

執行指令：

```bash
python -m unittest tests/test_task2.py -v
```

結果：

```text
test_root_tag_and_attrs ... ok
test_student_count_matches ... ok
test_student_attrs_exist ... ok
test_empty_student_list ... ok
test_xml_is_valid ... ok

Ran 5 tests in 0.003s

OK
```

讓測試通過的關鍵修改：

- 實作 `build_xml_tree(data)`
- 建立根節點 `<students>`
- 將 JSON 的 `學生清單` 逐筆轉成 `<student />`
- 確認每個 student 都有 `id`、`dept`、`school`、`zip` 屬性

### Refactor（重構紀錄）

執行指令：

```bash
python -m unittest tests/test_task2.py -v
```

結果：

```text
test_empty_student_list ... ok
test_read_json_rejects_non_object_root ... ok
test_root_tag_and_attrs ... ok
test_student_attrs_exist ... ok
test_student_count_matches ... ok
test_write_xml_file_can_be_read_back ... ok
test_xml_is_valid ... ok

Ran 7 tests in 0.006s

OK
```

重構內容：

- 補上型別提示
- 新增 `indent_xml()`，讓 XML 輸出更容易閱讀
- `read_json()` 檢查 JSON 根資料必須是 object/dict
- `write_xml()` 自動建立 `output/` 目錄
