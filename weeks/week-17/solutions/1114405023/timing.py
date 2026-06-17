"""
Week 17 - 0617 timing.py

提供 timeit 裝飾器：
- 可用 @timeit() 或 @timeit(repeat=次數)
- 每次呼叫會實際執行 repeat 次
- 每次耗時記錄到 wrapper.records
- 本次平均耗時記錄到 wrapper.last_elapsed
"""

from functools import wraps
from time import perf_counter


def timeit(func=None, *, repeat=3):
    """
    計算函式執行時間的裝飾器。

    Args:
        func: 被裝飾的函式。
        repeat: 每次呼叫時要重複執行的次數，預設為 3。

    Raises:
        ValueError: repeat 小於 1 時拋出。

    Returns:
        裝飾後的函式，且保留原本函式的回傳值。
    """
    # 輸入驗證要用 raise，不使用 assert，避免最佳化模式造成檢查失效。
    if repeat < 1:
        raise ValueError("repeat must be greater than or equal to 1")

    def decorator(real_func):
        @wraps(real_func)
        def wrapper(*args, **kwargs):
            total_elapsed = 0.0
            result = None

            for _ in range(repeat):
                start = perf_counter()
                result = real_func(*args, **kwargs)
                end = perf_counter()

                elapsed = end - start
                wrapper.records.append(elapsed)
                total_elapsed += elapsed

            wrapper.last_elapsed = total_elapsed / repeat
            return result

        # records 用來保存每一次實際執行的耗時紀錄。
        wrapper.records = []

        # last_elapsed 用來保存最近一次呼叫的平均耗時。
        wrapper.last_elapsed = 0.0

        return wrapper

    # 支援 @timeit 與 @timeit() 兩種寫法。
    if func is None:
        return decorator

    return decorator(func)
