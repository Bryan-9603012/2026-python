import unittest
from game.game import BigTwoGame
from game.models import Card


class TestGameSetup(unittest.TestCase):
    def test_game_has_4_players(self):
        game = BigTwoGame()
        game.setup()
        self.assertEqual(len(game.players), 4)

    def test_each_player_13_cards(self):
        game = BigTwoGame()
        game.setup()
        for player in game.players:
            self.assertEqual(len(player.hand), 13)

    def test_total_cards_distributed(self):
        game = BigTwoGame()
        game.setup()
        total = sum(len(player.hand) for player in game.players)
        self.assertEqual(total, 52)

    def test_first_player_has_3_clubs(self):
        game = BigTwoGame()
        game.setup()
        first_player = game.get_current_player()
        self.assertIsNotNone(first_player.hand.find_3_clubs())

    def test_one_human_three_ai(self):
        game = BigTwoGame()
        game.setup()
        human_count = sum(1 for p in game.players if not p.is_ai)
        ai_count = sum(1 for p in game.players if p.is_ai)
        self.assertEqual(human_count, 1)
        self.assertEqual(ai_count, 3)


class TestGamePlay(unittest.TestCase):
    def test_play_removes_cards(self):
        game = BigTwoGame()
        game.setup()
        card_3c = game.get_current_player().hand.find_3_clubs()
        if card_3c:
            game.play([card_3c])
            self.assertEqual(len(game.get_current_player().hand), 12)

    def test_play_sets_last_play(self):
        game = BigTwoGame()
        game.setup()
        card_3c = game.get_current_player().hand.find_3_clubs()
        if card_3c:
            game.play([card_3c])
            self.assertIsNotNone(game.last_play)

    def test_invalid_play(self):
        game = BigTwoGame()
        game.setup()
        card_not_3c = None
        for card in game.get_current_player().hand:
            if card.rank != 3 or card.suit != 0:
                card_not_3c = card
                break
        
        if card_not_3c:
            result = game.play([card_not_3c])
            self.assertFalse(result)

    def test_pass_increments(self):
        game = BigTwoGame()
        game.setup()
        card_3c = game.get_current_player().hand.find_3_clubs()
        if card_3c:
            game.play([card_3c])
            game.next_turn()
            result = game.pass_turn()
            if result:
                self.assertEqual(game.pass_count, 1)


class TestGameTurn(unittest.TestCase):
    def test_three_passes_resets(self):
        game = BigTwoGame()
        game.setup()
        card_3c = game.get_current_player().hand.find_3_clubs()
        if card_3c:
            game.play([card_3c])
            
            for _ in range(3):
                game.next_turn()
                game.pass_turn()
            
            self.assertIsNone(game.last_play)

    def test_turn_rotates(self):
        game = BigTwoGame()
        game.setup()
        first = game.current_player
        game.next_turn()
        self.assertEqual(game.current_player, (first + 1) % 4)


class TestGameWinner(unittest.TestCase):
    def test_detect_winner(self):
        game = BigTwoGame()
        game.setup()
        self.assertIsNone(game.get_winner())

    def test_no_winner_yet(self):
        game = BigTwoGame()
        game.setup()
        self.assertIsNone(game.get_winner())

    def test_game_ends(self):
        game = BigTwoGame()
        game.setup()
        self.assertFalse(game.is_game_over)


if __name__ == '__main__':
    unittest.main()
