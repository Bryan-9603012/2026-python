import unittest
from game.models import Card, Hand
from game.finder import HandFinder
from game.classifier import CardType


class TestFinderSingles(unittest.TestCase):
    def test_find_singles(self):
        f = HandFinder()
        hand = Hand([Card(14, 3), Card(13, 2), Card(3, 0)])
        result = f.find_singles(hand)
        self.assertEqual(len(result), 3)

    def test_find_singles_empty(self):
        f = HandFinder()
        hand = Hand([])
        result = f.find_singles(hand)
        self.assertEqual(len(result), 0)


class TestFinderPairs(unittest.TestCase):
    def test_find_pairs_one(self):
        f = HandFinder()
        hand = Hand([Card(14, 3), Card(14, 2), Card(3, 0)])
        result = f.find_pairs(hand)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0].rank, 14)

    def test_find_pairs_two(self):
        f = HandFinder()
        hand = Hand([Card(14, 3), Card(14, 2), Card(13, 3), Card(13, 2)])
        result = f.find_pairs(hand)
        self.assertEqual(len(result), 2)

    def test_find_pairs_none(self):
        f = HandFinder()
        hand = Hand([Card(14, 3), Card(13, 2), Card(3, 0)])
        result = f.find_pairs(hand)
        self.assertEqual(len(result), 0)


class TestFinderTriples(unittest.TestCase):
    def test_find_triples_one(self):
        f = HandFinder()
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(3, 0)])
        result = f.find_triples(hand)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0].rank, 14)

    def test_find_triples_with_extra(self):
        f = HandFinder()
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(13, 3), Card(13, 2)])
        result = f.find_triples(hand)
        self.assertEqual(len(result), 1)


class TestFinderFive(unittest.TestCase):
    def test_find_straight(self):
        f = HandFinder()
        hand = Hand([Card(3, 0), Card(4, 1), Card(5, 2), Card(6, 3), Card(7, 0), Card(14, 3)])
        result = f.find_straight(hand)
        self.assertGreater(len(result), 0)

    def test_find_flush(self):
        f = HandFinder()
        hand = Hand([Card(3, 0), Card(5, 0), Card(7, 0), Card(9, 0), Card(11, 0), Card(14, 1)])
        result = f.find_flush(hand)
        self.assertGreater(len(result), 0)

    def test_find_full_house(self):
        f = HandFinder()
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(13, 3), Card(13, 2)])
        result = f.find_full_house(hand)
        self.assertGreater(len(result), 0)

    def test_find_four_of_a_kind(self):
        f = HandFinder()
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 0), Card(3, 3)])
        result = f.find_four_of_a_kind(hand)
        self.assertGreater(len(result), 0)

    def test_find_straight_flush(self):
        f = HandFinder()
        hand = Hand([Card(3, 0), Card(4, 0), Card(5, 0), Card(6, 0), Card(7, 0), Card(14, 3)])
        result = f.find_straight_flush(hand)
        self.assertGreater(len(result), 0)


class TestFinderValidPlays(unittest.TestCase):
    def test_first_turn(self):
        f = HandFinder()
        hand = Hand([Card(3, 0), Card(14, 3), Card(13, 2)])
        result = f.find_valid_plays(hand, None, is_first=True)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0].rank, 3)
        self.assertEqual(result[0][0].suit, 0)

    def test_with_last_single(self):
        f = HandFinder()
        hand = Hand([Card(14, 3), Card(13, 2), Card(6, 1)])
        result = f.find_valid_plays(hand, (CardType.SINGLE, 5, 0))
        for play in result:
            self.assertEqual(len(play), 1)

    def test_with_last_pair(self):
        f = HandFinder()
        hand = Hand([Card(14, 3), Card(14, 2), Card(13, 2), Card(13, 1)])
        result = f.find_valid_plays(hand, (CardType.PAIR, 5, 0))
        for play in result:
            classified = f.classifier.classify(play)
            self.assertEqual(classified[0], CardType.PAIR)

    def test_no_valid(self):
        f = HandFinder()
        hand = Hand([Card(3, 0), Card(4, 1)])
        result = f.find_valid_plays(hand, (CardType.SINGLE, 14, 3))
        self.assertEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main()
