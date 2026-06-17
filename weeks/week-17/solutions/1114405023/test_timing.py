"""
Week 17 - 0617 timeit 測試檔
紅燈階段：先寫測試，再建立 timing.py。
"""

import unittest

from timing import timeit


class TestTimeitDecorator(unittest.TestCase):
    def test_return_value_should_not_change(self):
        """被裝飾函式的回傳值應該保持不變。"""

        @timeit()
        def add(a, b):
            """回傳兩數相加。"""
            return a + b

        result = add(2, 3)

        self.assertEqual(result, 5)

    def test_repeat_one_should_create_one_record(self):
        """repeat=1 時，records 應該只新增一筆時間紀錄。"""

        @timeit(repeat=1)
        def get_number():
            return 10

        result = get_number()

        self.assertEqual(result, 10)
        self.assertEqual(len(get_number.records), 1)
        self.assertIsInstance(get_number.last_elapsed, float)

    def test_default_repeat_should_create_three_records(self):
        """預設 repeat=3，所以每次呼叫應該新增三筆時間紀錄。"""

        @timeit()
        def get_number():
            return 100

        get_number()

        self.assertEqual(len(get_number.records), 3)
        self.assertIsInstance(get_number.last_elapsed, float)

    def test_invalid_repeat_should_raise_value_error(self):
        """repeat < 1 時，應該使用 raise ValueError，不可以用 assert。"""

        with self.assertRaises(ValueError):
            @timeit(repeat=0)
            def bad_func():
                return 1

    def test_should_keep_function_metadata(self):
        """使用 functools.wraps 保留原函式的 __name__ 與 __doc__。"""

        @timeit()
        def sample_func():
            """這是測試用函式。"""
            return 1

        self.assertEqual(sample_func.__name__, "sample_func")
        self.assertEqual(sample_func.__doc__, "這是測試用函式。")


if __name__ == "__main__":
    unittest.main()
