from pathlib import Path
import csv
from collections import Counter

import matplotlib.pyplot as plt
import numpy as np


def find_data_dir() -> Path:
    current = Path(__file__).resolve()

    for parent in current.parents:
        candidate = parent / "assets" / "stu-data"
        if candidate.exists():
            return candidate

    raise FileNotFoundError("找不到 assets/stu-data 資料夾")


DATA_DIR = find_data_dir()
YEARS = [112, 113, 114]


def setup_chinese_font() -> None:
    candidates = [
        "Microsoft JhengHei",
        "Noto Sans CJK TC",
        "Noto Sans CJK JP",
        "PingFang TC",
        "Heiti TC",
        "Arial Unicode MS",
    ]
    plt.rcParams["font.sans-serif"] = candidates
    plt.rcParams["axes.unicode_minus"] = False


def find_csv_file(year: int, data_dir: Path) -> Path:
    patterns = [
        f"{year}年新生資料庫.csv",
        f"{year}*新生資料庫*.csv",
        f"*{year}*新生*.csv",
        f"*{year}*.csv",
    ]

    for pattern in patterns:
        matches = sorted(data_dir.glob(pattern))
        if matches:
            return matches[0]

    raise FileNotFoundError(f"找不到 {year} 年的 CSV 檔案，搜尋位置：{data_dir}")


def load_year(year: int, data_dir: Path = DATA_DIR) -> dict[str, int]:
    """
    讀取單一年份 CSV，回傳 {系所名稱: 人數} 的 dict。
    """
    csv_path = find_csv_file(year, data_dir)
    counter: Counter[str] = Counter()

    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)

        if not reader.fieldnames or "系所名稱" not in reader.fieldnames:
            raise ValueError(f"{csv_path} 缺少「系所名稱」欄位")

        for row in reader:
            dept = (row.get("系所名稱") or "").strip()
            if dept:
                counter[dept] += 1

    return dict(counter)


def get_top_depts(year_data: dict[int, dict[str, int]], top_n: int = 8) -> list[str]:
    """
    從多年資料中找出任一年曾進前 top_n 的系所清單。
    """
    selected: list[str] = []

    for year in sorted(year_data):
        data = year_data[year]
        top_items = sorted(data.items(), key=lambda item: item[1], reverse=True)[:top_n]

        for dept, _count in top_items:
            if dept not in selected:
                selected.append(dept)

    return selected


def plot_grouped_bar(
    year_data: dict[int, dict[str, int]],
    depts: list[str],
    output_path: Path,
) -> None:
    setup_chinese_font()

    output_path.parent.mkdir(parents=True, exist_ok=True)

    years = sorted(year_data)
    y = np.arange(len(depts))
    bar_height = 0.22

    fig_height = max(6, len(depts) * 0.45)
    fig, ax = plt.subplots(figsize=(12, fig_height))

    for index, year in enumerate(years):
        values = [year_data[year].get(dept, 0) for dept in depts]
        offset = (index - (len(years) - 1) / 2) * bar_height
        bars = ax.barh(y + offset, values, height=bar_height, label=str(year))

        for bar, value in zip(bars, values):
            if value > 0:
                ax.text(
                    bar.get_width() + 0.5,
                    bar.get_y() + bar.get_height() / 2,
                    str(value),
                    va="center",
                    fontsize=8,
                )

    ax.set_yticks(y)
    ax.set_yticklabels(depts)
    ax.invert_yaxis()
    ax.set_xlabel("人數")
    ax.set_ylabel("系所名稱")
    ax.set_title("112、113、114 學年度各系招生人數比較")
    ax.legend(title="學年度")
    ax.grid(axis="x", linestyle="--", alpha=0.35)

    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)


def main() -> None:
    year_data = {year: load_year(year, DATA_DIR) for year in YEARS}
    depts = get_top_depts(year_data, top_n=8)

    output_path = Path(__file__).parent / "output" / "task1.png"
    plot_grouped_bar(year_data, depts, output_path)

    print(f"Task 1 圖表已輸出：{output_path}")


if __name__ == "__main__":
    main()