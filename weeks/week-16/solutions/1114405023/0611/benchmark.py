# benchmark.py
import json
import random
import time

from sorts import bubble_sort, quick_sort, merge_sort


def make_data(n: int, seed: int = 42) -> list:
    rng = random.Random(seed)
    return [rng.randint(0, n * 10) for _ in range(n)]


def measure_time(sort_func, data: list, repeats: int = 3) -> float:
    records = []

    for _ in range(repeats):
        copied_data = data.copy()

        start = time.perf_counter()
        sort_func(copied_data)
        end = time.perf_counter()

        records.append(end - start)

    return sum(records) / len(records)


def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    sort_functions = {
        "bubble_sort": bubble_sort,
        "quick_sort": quick_sort,
        "merge_sort": merge_sort,
    }

    results = {}

    for size in sizes:
        data = make_data(size)
        results[str(size)] = {}

        for name, sort_func in sort_functions.items():
            elapsed = measure_time(sort_func, data, repeats)
            results[str(size)][name] = elapsed

    return results


def print_results_table(results: dict) -> None:
    print(f"{'Size':<10}{'Bubble Sort':<18}{'Quick Sort':<18}{'Merge Sort':<18}")
    print("-" * 64)

    for size, row in results.items():
        print(
            f"{size:<10}"
            f"{row['bubble_sort']:<18.6f}"
            f"{row['quick_sort']:<18.6f}"
            f"{row['merge_sort']:<18.6f}"
        )


def save_results(results: dict, filename: str = "results.json") -> None:
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)


if __name__ == "__main__":
    benchmark_results = run_benchmark()
    print_results_table(benchmark_results)
    save_results(benchmark_results)