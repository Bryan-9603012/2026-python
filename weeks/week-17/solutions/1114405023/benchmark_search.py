"""
Week 17 - 0617 搜尋效能評估

執行方式：
python .\benchmark_search.py

注意：
需要同一個資料夾內已經有 timing.py 與 search.py。
"""

from timing import timeit
from search import linear_search, binary_search


DATA_SIZE = 100000
TARGET = DATA_SIZE - 1


@timeit(repeat=5)
def run_linear_search():
    data = list(range(DATA_SIZE))
    return linear_search(data, TARGET)


@timeit(repeat=5)
def run_binary_search():
    data = list(range(DATA_SIZE))
    return binary_search(data, TARGET)


def main():
    linear_result = run_linear_search()
    binary_result = run_binary_search()

    print("linear_search result:", linear_result)
    print("linear_search records:", run_linear_search.records)
    print("linear_search average:", run_linear_search.last_elapsed)

    print("binary_search result:", binary_result)
    print("binary_search records:", run_binary_search.records)
    print("binary_search average:", run_binary_search.last_elapsed)

    if run_binary_search.last_elapsed > 0:
        ratio = run_linear_search.last_elapsed / run_binary_search.last_elapsed
        print("linear / binary ratio:", ratio)


if __name__ == "__main__":
    main()
