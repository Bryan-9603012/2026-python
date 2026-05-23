from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from task2_zipcode_heatmap import (
    DATA_DIR,
    YEARS,
    zip_to_county,
    load_county_counts,
    get_top_counties,
)


class TestTask2(unittest.TestCase):
    def test_zip_to_county_penghu(self):
        self.assertEqual(zip_to_county("880"), "澎湖縣")

    def test_zip_to_county_unknown(self):
        self.assertEqual(zip_to_county("999"), "其他")

    def test_load_county_counts_type(self):
        result = load_county_counts(112, DATA_DIR)

        self.assertIsInstance(result, dict)
        self.assertGreater(len(result), 0)

    def test_load_county_counts_penghu_positive(self):
        result = load_county_counts(112, DATA_DIR)

        self.assertGreater(result.get("澎湖縣", 0), 0)

    def test_get_top_counties_length(self):
        all_years = {
            year: load_county_counts(year, DATA_DIR)
            for year in YEARS
        }

        result = get_top_counties(all_years, top_n=10)

        self.assertLessEqual(len(result), 10)
        self.assertGreater(len(result), 0)


if __name__ == "__main__":
    unittest.main()