"""
Week 10 Task 1: CSV -> JSON

功能：
1. 讀取 Week 08 的 NPU 新生資料 CSV
2. 篩選「入學方式 == 聯合登記分發」
3. 統計各系所人數
4. 輸出 output/students.json
"""

from __future__ import annotations

import csv
import functools
import json
import time
from pathlib import Path
from typing import Any


DEFAULT_CSV_PATH = Path("../../week-08/in-class/stu-data/113年新生資料庫.csv")
DEFAULT_OUTPUT_PATH = Path("output/students.json")
ADMISSION_METHOD = "聯合登記分發"


def timeit(func):
    """量測函式執行時間的裝飾器。"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[timeit] {func.__name__} 耗時 {elapsed:.6f}s")
        return result

    return wrapper


@timeit
def read_csv(filepath: str | Path) -> list[dict[str, str]]:
    """讀取 CSV，回傳所有列的 list。CSV 使用 UTF-8-BOM，所以 encoding 使用 utf-8-sig。"""
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"找不到 CSV 檔案：{path}")

    with path.open("r", encoding="utf-8-sig", newline="") as fp:
        reader = csv.DictReader(fp)
        return [dict(row) for row in reader]


@timeit
def write_json(data: dict[str, Any], filepath: str | Path) -> None:
    """將資料寫出為 JSON 檔案。"""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as fp:
        json.dump(data, fp, ensure_ascii=False, indent=2)


def filter_by_admission(rows: list[dict[str, str]], method: str) -> list[dict[str, str]]:
    """依照入學方式過濾學生資料。"""
    return [row for row in rows if row.get("入學方式") == method]


def count_by_dept(rows: list[dict[str, str]]) -> dict[str, int]:
    """統計每個系所名稱出現的人數。"""
    counts: dict[str, int] = {}
    for row in rows:
        dept = row.get("系所名稱", "").strip()
        if not dept:
            continue
        counts[dept] = counts.get(dept, 0) + 1
    return counts


def build_output_data(rows: list[dict[str, str]], method: str = ADMISSION_METHOD) -> dict[str, Any]:
    """把篩選後的學生資料整理成作業指定的 JSON 格式。"""
    filtered = filter_by_admission(rows, method)

    students = [
        {
            "學號": row.get("學號", ""),
            "系所名稱": row.get("系所名稱", ""),
            "畢業學校": row.get("畢業學校", ""),
            "郵遞區號": row.get("郵遞區號", ""),
        }
        for row in filtered
    ]

    return {
        "來源": "113年新生資料庫",
        "入學方式篩選": method,
        "總人數": len(students),
        "系所統計": count_by_dept(filtered),
        "學生清單": students,
    }


def main() -> None:
    """執行 Task 1：CSV -> JSON。"""
    rows = read_csv(DEFAULT_CSV_PATH)
    data = build_output_data(rows, ADMISSION_METHOD)
    write_json(data, DEFAULT_OUTPUT_PATH)

    print(f"已輸出 JSON：{DEFAULT_OUTPUT_PATH}")
    print(f"篩選入學方式：{ADMISSION_METHOD}")
    print(f"總人數：{data['總人數']}")


if __name__ == "__main__":
    main()
