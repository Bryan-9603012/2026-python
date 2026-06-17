"""
Week 17 - 0617 search.py

提供兩種搜尋方式：
1. linear_search：線性搜尋
2. binary_search：二分搜尋

注意：
binary_search 的前提是 data 必須已經由小到大排序。
本版本若收到未排序資料，會 raise ValueError。
"""


def _is_sorted(data):
    """檢查資料是否已由小到大排序。"""
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True


def linear_search(data: list, target) -> int:
    """
    逐一比對資料，找到 target 就回傳 index，找不到回傳 -1。

    Args:
        data: 要搜尋的 list。
        target: 要尋找的目標值。

    Returns:
        int: 找到回傳 index，找不到回傳 -1。
    """
    for index, value in enumerate(data):
        if value == target:
            return index

    return -1


def binary_search(data: list, target) -> int:
    """
    使用二分搜尋尋找 target。

    前提：
        data 必須已經由小到大排序。

    未排序資料的行為：
        若 data 未排序，本函式會 raise ValueError，
        因為二分搜尋需要依靠排序結果判斷要往左半邊或右半邊尋找。

    Args:
        data: 已排序的 list。
        target: 要尋找的目標值。

    Returns:
        int: 找到回傳 index，找不到回傳 -1。

    Raises:
        ValueError: data 未排序時拋出。
    """
    if not _is_sorted(data):
        raise ValueError("binary_search requires sorted data")

    left = 0
    right = len(data) - 1

    while left <= right:
        middle = (left + right) // 2

        if data[middle] == target:
            return middle

        if data[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1
