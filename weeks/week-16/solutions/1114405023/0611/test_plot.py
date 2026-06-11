import os
import shutil
import unittest

from plot import plot_benchmark


class TestPlotBenchmark(unittest.TestCase):
    def setUp(self):
        os.makedirs("assets", exist_ok=True)

    def tearDown(self):
        if os.path.exists("assets"):
            shutil.rmtree("assets")

    def test_plot_benchmark_creates_png_file(self):
        plot_benchmark("results.json", "assets/benchmark.png")

        self.assertTrue(os.path.exists("assets/benchmark.png"))
        self.assertGreater(os.path.getsize("assets/benchmark.png"), 0)


if __name__ == "__main__":
    unittest.main()