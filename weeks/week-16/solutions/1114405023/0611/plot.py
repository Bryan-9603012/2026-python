# plot.py
import json
import os

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt


def plot_benchmark(
    input_file: str = "results.json",
    output_file: str = "assets/benchmark.png",
) -> None:
    with open(input_file, "r", encoding="utf-8") as file:
        results = json.load(file)

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    sizes = [int(size) for size in results.keys()]
    first_size = next(iter(results))
    sort_names = list(results[first_size].keys())

    for sort_name in sort_names:
        times = [results[str(size)][sort_name] for size in sizes]
        plt.plot(sizes, times, marker="o", label=sort_name)

    plt.xlabel("Input Size")
    plt.ylabel("Average Time (seconds)")
    plt.yscale("log")
    plt.title("Sorting Algorithm Benchmark")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(output_file)
    plt.close()


if __name__ == "__main__":
    plot_benchmark()