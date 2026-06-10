"""Stage 4 — 繪圖輸出測試

規格: plot.py 的 load_results / plot_results 必須
  1. load_results(path) 回傳 dict,內容為各演算法各 n 的平均耗時
  2. plot_results(results, out_path) 產生 PNG 圖檔
  3. 產生之 PNG 非空檔
"""

import os
import json
import unittest

# from plot import load_results, plot_results  # 完成 plot.py 後解除註解


class TestPlot(unittest.TestCase):
    """繪圖功能驗證"""

    def setUp(self):
        """建立測試用 results.json"""
        self.test_json = "/tmp/_test_results.json"
        self.test_png = "/tmp/_test_plot.png"
        self.sample_data = {
            "bubble_sort": {
                "500": {"mean": 0.006, "records": [0.005, 0.006, 0.007]},
                "1000": {"mean": 0.028, "records": [0.027, 0.028, 0.029]},
            },
            "quick_sort": {
                "500": {"mean": 0.0004, "records": [0.0004, 0.0004, 0.0005]},
                "1000": {"mean": 0.0008, "records": [0.0008, 0.0009, 0.0008]},
            },
        }
        with open(self.test_json, "w") as f:
            json.dump(self.sample_data, f)

    def tearDown(self):
        """清除測試暫存檔"""
        for p in [self.test_json, self.test_png]:
            if os.path.exists(p):
                os.remove(p)

    def test_load_results_returns_dict(self):
        """載入 results.json 回傳 dict"""
        self.fail("尚未實作")

    def test_load_results_has_expected_keys(self):
        """dict 包含各演算法名稱作為 key"""
        self.fail("尚未實作")

    def test_plot_results_creates_png(self):
        """plot_results 產生 PNG 檔案"""
        self.fail("尚未實作")

    # ── Edge cases ──

    def test_plot_results_png_not_empty(self):
        """EDGE: 產生之 PNG 檔案大小大於 0"""
        self.fail("尚未實作")

    def test_load_results_file_not_found(self):
        """EDGE: 不存在的路徑拋出 FileNotFoundError"""
        self.fail("尚未實作")


if __name__ == "__main__":
    unittest.main()
