"""Plot benchmark results for Stage 4."""

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt


def load_results(path: str) -> dict:
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def plot_results(results: dict, out_path: str) -> None:
    sizes = results["sizes"]
    algorithms = results["algorithms"]
    if not algorithms:
        raise ValueError("results must include at least one algorithm")

    output = Path(out_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(9, 5))
    for name, timings in algorithms.items():
        averages = [timings[str(size)]["average"] for size in sizes]
        ax.plot(sizes, averages, marker="o", label=name)

    ax.set_title("Sorting Algorithm Benchmark")
    ax.set_xlabel("Input size (n)")
    ax.set_ylabel("Average time (seconds)")
    ax.set_yscale("log")
    ax.grid(True, which="both", linestyle="--", linewidth=0.5)
    ax.legend()
    fig.tight_layout()
    fig.savefig(output)
    plt.close(fig)


def main() -> None:
    results = load_results("results.json")
    plot_results(results, "assets/benchmark.png")


if __name__ == "__main__":
    main()
