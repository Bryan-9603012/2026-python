import unittest

from benchmark import make_data, run_benchmark


class TestSecurityAndValidation(unittest.TestCase):
    def test_make_data_rejects_negative_size(self):
        with self.assertRaises(ValueError):
            make_data(-1)

    def test_make_data_rejects_non_integer_size(self):
        with self.assertRaises(TypeError):
            make_data("100")

    def test_run_benchmark_rejects_zero_repeats(self):
        with self.assertRaises(ValueError):
            run_benchmark(sizes=(10,), repeats=0)

    def test_run_benchmark_rejects_negative_repeats(self):
        with self.assertRaises(ValueError):
            run_benchmark(sizes=(10,), repeats=-1)


if __name__ == "__main__":
    unittest.main()