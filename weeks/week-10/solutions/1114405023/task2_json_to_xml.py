"""
Week 10 Task 2: JSON -> XML

功能：
1. 讀取 Task 1 產生的 output/students.json
2. 將學生清單轉成 XML
3. 輸出 output/students.xml
"""

from __future__ import annotations

import functools
import json
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any


DEFAULT_JSON_PATH = Path("output/students.json")
DEFAULT_OUTPUT_PATH = Path("output/students.xml")


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
def read_json(filepath: str | Path) -> dict[str, Any]:
    """讀取 JSON 檔案，回傳 dict。"""
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"找不到 JSON 檔案：{path}")

    with path.open("r", encoding="utf-8") as fp:
        data = json.load(fp)

    if not isinstance(data, dict):
        raise ValueError("JSON 根資料必須是 dict/object 格式")

    return data


def build_xml_tree(data: dict[str, Any]) -> ET.Element:
    """建構 ElementTree 結構，回傳根節點。"""
    students = data.get("學生清單", [])
    if not isinstance(students, list):
        raise ValueError("學生清單必須是 list 格式")

    total = data.get("總人數", len(students))
    root = ET.Element(
        "students",
        {
            "source": str(data.get("來源", "")),
            "total": str(total),
        },
    )

    for student in students:
        if not isinstance(student, dict):
            continue

        ET.SubElement(
            root,
            "student",
            {
                "id": str(student.get("學號", "")),
                "dept": str(student.get("系所名稱", "")),
                "school": str(student.get("畢業學校", "")),
                "zip": str(student.get("郵遞區號", "")),
            },
        )

    return root


def indent_xml(element: ET.Element, level: int = 0) -> None:
    """讓 XML 輸出有縮排，提升可讀性。"""
    indent = "\n" + level * "  "
    child_indent = "\n" + (level + 1) * "  "

    children = list(element)
    if children:
        if not element.text or not element.text.strip():
            element.text = child_indent
        for child in children:
            indent_xml(child, level + 1)
        if not element.tail or not element.tail.strip():
            element.tail = indent
    else:
        if level and (not element.tail or not element.tail.strip()):
            element.tail = indent


@timeit
def write_xml(data: dict[str, Any], filepath: str | Path) -> None:
    """將 dict 轉換為 XML 並寫出。"""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    root = build_xml_tree(data)
    indent_xml(root)
    tree = ET.ElementTree(root)
    tree.write(path, encoding="utf-8", xml_declaration=True)


def main() -> None:
    """執行 Task 2：JSON -> XML。"""
    data = read_json(DEFAULT_JSON_PATH)
    write_xml(data, DEFAULT_OUTPUT_PATH)
    print(f"已輸出 XML：{DEFAULT_OUTPUT_PATH}")


if __name__ == "__main__":
    main()
