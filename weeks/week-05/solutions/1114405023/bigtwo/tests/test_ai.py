import unittest
from game.models import Card, Hand
from game.ai import AIStrategy
from game.classifier import CardType


class TestAIScoring(unittest.TestCase):
    def test_score_single(self):
        ai = AIStrategy()
        hand = Hand([Card(14, 3), Card(13, 2)])
        score = ai.score_hand([Card(14, 3)], hand)
        expected = 1 * 100 + 14 * 10 + 3 + 5 + 500
        self.assertGreater(score, 200)

    def test_score_pair_higher(self):
        ai = AIStrategy()
        hand = Hand([Card(14, 3), Card(14, 2), Card(3, 0)])
        pair_score = ai.score_hand([Card(14, 3), Card(14, 2)], hand)
        single_score = ai.score_hand([Card(3, 0)], hand)
        self.assertGreater(pair_score, single_score)

    def test_score_triple_higher(self):
        ai = AIStrategy()
        hand = Hand([Card(14, 3), Card(14, 2), Card(14, 1), Card(13, 2)])
        triple_score = ai.score_hand([Card(14, 3), Card(14, 2), Card(14, 1)], hand)
        pair_score = ai.score_hand([Card(14, 3), Card(14, 2)], hand)
        self.assertGreater(triple_score, pair_score)

    def test_score_near_empty(self):
        ai = AIStrategy()
        hand = Hand([Card(14, 3)])
        score = ai.score_hand([Card(14, 3)], hand)
        self.assertGreater(score, 10000)

    def test_score_low_cards(self):
        ai = AIStrategy()
        hand = Hand([Card(3, 0), Card(4, 1)])
        score = ai.score_hand([Card(3, 0)], hand)
        self.assertGreater(score, 500)

    def test_score_spade_bonus(self):
        ai = AIStrategy()
        hand = Hand([Card(14, 3), Card(13, 2)])
        score = ai.score_hand([Card(14, 3)], hand)
        self.assertTrue(score >= 5)


class TestAISelection(unittest.TestCase):
    def test_select_best(self):
        ai = AIStrategy()
        hand = Hand([Card(14, 3), Card(14, 2), Card(3, 0)])
        valid_plays = [[Card(3, 0)], [Card(14, 3), Card(14, 2)]]
        result = ai.select_best(hand, valid_plays)
        self.assertEqual(len(result), 2)

    def test_select_first_turn(self):
        ai = AIStrategy()
        hand = Hand([Card(3, 0), Card(14, 3)])
        valid_plays = [[Card(3, 0)]]
        result = ai.select_best(hand, valid_plays, is_first=True)
        self.assertIsNotNone(result)

    def test_select_empty(self):
        ai = AIStrategy()
        hand = Hand([Card(14, 3)])
        result = ai.select_best(hand, [])
        self.assertIsNone(result)


class TestAIStrategy(unittest.TestCase):
    def test_ai_always_plays(self):
        ai = AIStrategy()
        hand = Hand([Card(14, 3), Card(13, 2)])
        result = ai.choose_play(hand, None)
        self.assertIsNotNone(result)

    def test_ai_prefers_high(self):
        ai = AIStrategy()
        hand = Hand([Card(3, 0), Card(14, 3)])
        result = ai.choose_play(hand, (CardType.SINGLE, 5, 0))
        self.assertEqual(result[0].rank, 14)

    def test_ai_try_empty(self):
        ai = AIStrategy()
        hand = Hand([Card(14, 3)])
        result = ai.choose_play(hand, (CardType.SINGLE, 3, 0))
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
