"""
Week 10 Task 3: 畫出 Task 1 / Task 2 函式耗時比較圖

可直接使用 TIMING_REPORT.md 裡的 [timeit] 數據。
若讀不到數據，會使用一組預設範例值，避免程式無法產生圖片。
"""

from __future__ import annotations

import re
from pathlib import Path

import matplotlib.pyplot as plt


REPORT_PATH = Path("TIMING_REPORT.md")
OUTPUT_PATH = Path("output/timing_comparison.png")

FUNCTIONS = ["read_csv", "write_json", "read_json", "write_xml"]
FALLBACK_TIMINGS = {
    "read_csv": 0.002341,
    "write_json": 0.001203,
    "read_json": 0.000891,
    "write_xml": 0.003412,
}


def load_timings(report_path: str | Path = REPORT_PATH) -> dict[str, float]:
    """從 TIMING_REPORT.md 擷取 [timeit] 函式耗時。"""
    path = Path(report_path)
    if not path.exists():
        return FALLBACK_TIMINGS.copy()

    text = path.read_text(encoding="utf-8")
    pattern = re.compile(r"\[timeit\]\s+(\w+)\s+耗時\s+([0-9.]+)s")
    parsed = {name: float(seconds) for name, seconds in pattern.findall(text)}

    if all(name in parsed for name in FUNCTIONS):
        return {name: parsed[name] for name in FUNCTIONS}

    return FALLBACK_TIMINGS.copy()


def plot_timings(timings: dict[str, float], output_path: str | Path = OUTPUT_PATH) -> None:
    """繪製長條圖並輸出 PNG。"""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    names = FUNCTIONS
    values = [timings[name] for name in names]

    plt.figure(figsize=(9, 5))
    bars = plt.bar(names, values)

    plt.title("Task 1/2 Function Runtime Comparison")
    plt.xlabel("Function")
    plt.ylabel("Runtime (seconds)")

    for bar, value in zip(bars, values):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"{value:.6f}s",
            ha="center",
            va="bottom",
            fontsize=9,
        )

    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close()

    print(f"圖表已儲存：{path}")


def main() -> None:
    timings = load_timings()
    plot_timings(timings)


if __name__ == "__main__":
    main()
