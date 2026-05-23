from pathlib import Path
import sys
import csv
from collections import Counter
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from task1_grouped_bar import DATA_DIR, load_year, get_top_depts, find_csv_file


class TestTask1(unittest.TestCase):
    def test_load_year_returns_dict(self):
        result = load_year(112, DATA_DIR)

        self.assertIsInstance(result, dict)
        self.assertGreater(len(result), 0)
        self.assertTrue(all(isinstance(key, str) for key in result.keys()))

    def test_load_year_counts_correct(self):
        csv_path = find_csv_file(112, DATA_DIR)

        with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            counter = Counter(
                (row.get("系所名稱") or "").strip()
                for row in reader
                if (row.get("系所名稱") or "").strip()
            )

        expected_dept, expected_count = counter.most_common(1)[0]
        result = load_year(112, DATA_DIR)

        self.assertEqual(result[expected_dept], expected_count)

    def test_load_year_total_positive(self):
        result = load_year(113, DATA_DIR)
        total = sum(result.values())

        self.assertGreater(total, 0)

    def test_get_top_depts_length(self):
        year_data = {
            112: load_year(112, DATA_DIR),
            113: load_year(113, DATA_DIR),
            114: load_year(114, DATA_DIR),
        }

        result = get_top_depts(year_data, top_n=8)

        self.assertLessEqual(len(result), 24)
        self.assertGreater(len(result), 0)

    def test_get_top_depts_includes_popular(self):
        year_data = {
            112: load_year(112, DATA_DIR),
            113: load_year(113, DATA_DIR),
            114: load_year(114, DATA_DIR),
        }

        popular_dept = max(year_data[112].items(), key=lambda item: item[1])[0]
        result = get_top_depts(year_data, top_n=8)

        self.assertIn(popular_dept, result)


if __name__ == "__main__":
    unittest.main()