import unittest
from game.models import Card
from game.classifier import CardType, HandClassifier


class TestCardType(unittest.TestCase):
    def test_cardtype_values(self):
        self.assertEqual(CardType.SINGLE, 1)
        self.assertEqual(CardType.PAIR, 2)
        self.assertEqual(CardType.TRIPLE, 3)
        self.assertEqual(CardType.STRAIGHT, 4)
        self.assertEqual(CardType.FLUSH, 5)
        self.assertEqual(CardType.FULL_HOUSE, 6)
        self.assertEqual(CardType.FOUR_OF_A_KIND, 7)
        self.assertEqual(CardType.STRAIGHT_FLUSH, 8)


class TestClassifierSingle(unittest.TestCase):
    def test_classify_single_ace(self):
        c = HandClassifier()
        result = c.classify([Card(14, 3)])
        self.assertEqual(result, (CardType.SINGLE, 14, 3))

    def test_classify_single_two(self):
        c = HandClassifier()
        result = c.classify([Card(15, 0)])
        self.assertEqual(result, (CardType.SINGLE, 15, 0))

    def test_classify_single_three(self):
        c = HandClassifier()
        result = c.classify([Card(3, 0)])
        self.assertEqual(result, (CardType.SINGLE, 3, 0))


class TestClassifierPair(unittest.TestCase):
    def test_classify_pair(self):
        c = HandClassifier()
        result = c.classify([Card(14, 3), Card(14, 2)])
        self.assertEqual(result[0], CardType.PAIR)
        self.assertEqual(result[1], 14)

    def test_classify_pair_diff_rank(self):
        c = HandClassifier()
        result = c.classify([Card(14, 3), Card(13, 3)])
        self.assertIsNone(result)

    def test_classify_pair_from_three(self):
        c = HandClassifier()
        result = c.classify([Card(14, 3), Card(14, 2)])
        self.assertEqual(result[0], CardType.PAIR)
        self.assertEqual(result[1], 14)


class TestClassifierTriple(unittest.TestCase):
    def test_classify_triple(self):
        c = HandClassifier()
        result = c.classify([Card(14, 3), Card(14, 2), Card(14, 1)])
        self.assertEqual(result, (CardType.TRIPLE, 14, 0))

    def test_classify_triple_not_enough(self):
        c = HandClassifier()
        result = c.classify([Card(14, 3), Card(13, 2)])
        self.assertIsNone(result)


class TestClassifierFive(unittest.TestCase):
    def test_classify_straight(self):
        c = HandClassifier()
        result = c.classify([Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0)])
        self.assertEqual(result[0], CardType.STRAIGHT)
        self.assertEqual(result[1], 7)

    def test_classify_straight_ace_low(self):
        c = HandClassifier()
        result = c.classify([Card(14, 0), Card(15, 1), Card(3, 2), Card(4, 3), Card(5, 0)])
        self.assertEqual(result[0], CardType.STRAIGHT)

    def test_classify_flush(self):
        c = HandClassifier()
        result = c.classify([Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0)])
        self.assertEqual(result[0], CardType.FLUSH)
        self.assertEqual(result[1], 11)

    def test_classify_full_house(self):
        c = HandClassifier()
        result = c.classify([Card(14, 3), Card(14, 2), Card(14, 1), Card(15, 0), Card(15, 3)])
        self.assertEqual(result[0], CardType.FULL_HOUSE)
        self.assertEqual(result[1], 14)

    def test_classify_four_of_a_kind(self):
        c = HandClassifier()
        result = c.classify([Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 0), Card(3, 3)])
        self.assertEqual(result[0], CardType.FOUR_OF_A_KIND)
        self.assertEqual(result[1], 14)

    def test_classify_straight_flush(self):
        c = HandClassifier()
        result = c.classify([Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0)])
        self.assertEqual(result[0], CardType.STRAIGHT_FLUSH)
        self.assertEqual(result[1], 7)


class TestClassifierCompare(unittest.TestCase):
    def test_compare_single_rank(self):
        c = HandClassifier()
        h1 = (CardType.SINGLE, 14, 3)
        h2 = (CardType.SINGLE, 13, 3)
        self.assertEqual(c.compare(h1, h2), 1)

    def test_compare_single_suit(self):
        c = HandClassifier()
        h1 = (CardType.SINGLE, 14, 3)
        h2 = (CardType.SINGLE, 14, 2)
        self.assertEqual(c.compare(h1, h2), 1)

    def test_compare_pair_rank(self):
        c = HandClassifier()
        h1 = (CardType.PAIR, 14, 0)
        h2 = (CardType.PAIR, 13, 0)
        self.assertEqual(c.compare(h1, h2), 1)

    def test_compare_pair_suit(self):
        c = HandClassifier()
        h1 = (CardType.PAIR, 14, 2)
        h2 = (CardType.PAIR, 14, 0)
        self.assertEqual(c.compare(h1, h2), 1)

    def test_compare_different_type(self):
        c = HandClassifier()
        h1 = (CardType.PAIR, 14, 0)
        h2 = (CardType.SINGLE, 14, 3)
        self.assertEqual(c.compare(h1, h2), 1)

    def test_compare_flush_vs_straight(self):
        c = HandClassifier()
        h1 = (CardType.FLUSH, 14, 0)
        h2 = (CardType.STRAIGHT, 14, 0)
        self.assertEqual(c.compare(h1, h2), 1)


class TestClassifierCanPlay(unittest.TestCase):
    def test_can_play_first_3clubs(self):
        c = HandClassifier()
        result = c.can_play(None, [Card(3, 0)], is_first=True)
        self.assertTrue(result)

    def test_can_play_first_not_3clubs(self):
        c = HandClassifier()
        result = c.can_play(None, [Card(14, 3)], is_first=True)
        self.assertFalse(result)

    def test_can_play_same_type(self):
        c = HandClassifier()
        last = (CardType.SINGLE, 5, 0)
        new = (CardType.SINGLE, 6, 0)
        self.assertTrue(c.can_play(last, new))

    def test_can_play_diff_type(self):
        c = HandClassifier()
        last = (CardType.PAIR, 5, 0)
        new = (CardType.SINGLE, 6, 0)
        self.assertFalse(c.can_play(last, new))

    def test_can_play_not_stronger(self):
        c = HandClassifier()
        last = (CardType.PAIR, 10, 0)
        new = (CardType.PAIR, 5, 0)
        self.assertFalse(c.can_play(last, new))


if __name__ == '__main__':
    unittest.main()
