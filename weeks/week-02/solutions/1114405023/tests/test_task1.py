import unittest
from task1_sequence_clean import sequence_clean


class TestSequenceClean(unittest.TestCase):

    def test_normal(self):
        nums = [5,3,5,2,9,2,8,3,1]
        dedupe, asc, desc, evens = sequence_clean(nums)

        self.assertEqual(dedupe, [5,3,2,9,8,1])
        self.assertEqual(asc, [1,2,2,3,3,5,5,8,9])
        self.assertEqual(desc, [9,8,5,5,3,3,2,2,1])
        self.assertEqual(evens, [2,2,8])

    def test_empty(self):
        nums = []
        dedupe, asc, desc, evens = sequence_clean(nums)

        self.assertEqual(dedupe, [])
        self.assertEqual(asc, [])
        self.assertEqual(desc, [])
        self.assertEqual(evens, [])

    def test_all_duplicates(self):
        nums = [3,3,3]
        dedupe, asc, desc, evens = sequence_clean(nums)

        self.assertEqual(dedupe, [3])