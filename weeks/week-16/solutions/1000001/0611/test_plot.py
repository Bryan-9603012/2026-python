"""Stage 4 — plot output tests."""

import json
import tempfile
import unittest
from pathlib import Path

from plot import load_results, plot_results


SAMPLE_RESULTS = {
    "sizes": [10, 20],
    "repeats": 1,
    "algorithms": {
        "quick_sort": {
            "10": {"records": [0.001], "average": 0.001},
            "20": {"records": [0.002], "average": 0.002},
        },
        "builtin_sort": {
            "10": {"records": [0.0001], "average": 0.0001},
            "20": {"records": [0.0002], "average": 0.0002},
        },
    },
}


class TestPlotResults(unittest.TestCase):
    def test_load_results_reads_json(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            path = Path(tmp_dir) / "results.json"
            path.write_text(json.dumps(SAMPLE_RESULTS), encoding="utf-8")

            self.assertEqual(load_results(str(path)), SAMPLE_RESULTS)

    def test_plot_results_creates_non_empty_png(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            out_path = Path(tmp_dir) / "benchmark.png"

            plot_results(SAMPLE_RESULTS, str(out_path))

            self.assertTrue(out_path.exists())
            self.assertGreater(out_path.stat().st_size, 0)
            self.assertEqual(out_path.read_bytes()[:8], b"\x89PNG\r\n\x1a\n")

    def test_plot_results_creates_parent_directory(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            out_path = Path(tmp_dir) / "assets" / "benchmark.png"

            plot_results(SAMPLE_RESULTS, str(out_path))

            self.assertTrue(out_path.exists())
            self.assertGreater(out_path.stat().st_size, 0)

    def test_plot_results_rejects_empty_algorithms(self):
        empty_results = {
            "sizes": [10],
            "repeats": 1,
            "algorithms": {},
        }

        with tempfile.TemporaryDirectory() as tmp_dir:
            out_path = Path(tmp_dir) / "benchmark.png"
            with self.assertRaises(ValueError):
                plot_results(empty_results, str(out_path))


if __name__ == "__main__":
    unittest.main()
