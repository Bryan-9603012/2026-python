# TEST_CASES

## Task1 — sequence_clean

### TC1: Normal case（對應：tests/test_task1.py::test_sequence_clean）

**Input**
- nums = [1, 2, 3, 2, 4, 5, 1]

**Expected Output**
- dedupe = [1, 2, 3, 4, 5]
- asc    = [1, 1, 2, 2, 3, 4, 5]
- desc   = [5, 4, 3, 2, 2, 1, 1]
- evens  = [2, 2, 4]

**Purpose**
- 驗證基本功能：去重（保留順序）、升序、降序、偶數擷取（保留原順序）

**Result**
- PASS


---

### TC2: Edge case - empty list（對應：tests/test_task1.py::test_empty_list）

**Input**
- nums = []

**Expected Output**
- dedupe = []
- asc    = []
- desc   = []
- evens  = []

**Purpose**
- 驗證空輸入不會出錯，且四個輸出皆為空列表

**Result**
- PASS


---

### TC3: Negative/Unusual case - all duplicates（對應：tests/test_task1.py::test_all_duplicates）

**Input**
- nums = [1, 1, 1, 1]

**Expected Output**
- dedupe = [1]
- asc    = [1, 1, 1, 1]
- desc   = [1, 1, 1, 1]
- evens  = []

**Purpose**
- 驗證「全部重複」時，去重結果只保留第一次出現的元素
- 同時確認排序仍保留所有元素、偶數結果正確

**Result**
- PASS