import unittest
import pygame
from unittest.mock import Mock, patch
from game.models import Card, Hand
from game.ui import CardRenderer, HandRenderer, BigTwoUI


pygame.init()


class TestCardRenderer(unittest.TestCase):
    def test_card_render(self):
        surface = pygame.display.set_mode((100, 100))
        CardRenderer.render(surface, Card(14, 3), 0, 0)
        self.assertIsNotNone(surface)
        pygame.display.quit()

    def test_hand_render(self):
        surface = pygame.display.set_mode((500, 200))
        renderer = HandRenderer()
        hand = Hand([Card(14, 3), Card(13, 2), Card(3, 0)])
        renderer.render(surface, hand, 0, 0)
        self.assertIsNotNone(surface)
        pygame.display.quit()


class TestUI(unittest.TestCase):
    def test_game_init(self):
        with patch('pygame.init'):
            ui = BigTwoUI()
            self.assertEqual(len(ui.game.players), 4)

    def test_card_selection(self):
        with patch('pygame.init'):
            ui = BigTwoUI()
            player = ui.game.players[0]
            player.hand = Hand([Card(14, 3), Card(13, 2)])
            
            card = ui.human_hand_renderer.handle_click((120, 500), player.hand, 100, 500)
            self.assertIsNotNone(card)
            self.assertEqual(len(ui.human_hand_renderer.get_selected()), 1)

    def test_button_click(self):
        with patch('pygame.init'):
            ui = BigTwoUI()
            
            result = ui.play_button_rect.collidepoint(400, 500)
            self.assertTrue(result)
            
            result = ui.pass_button_rect.collidepoint(400, 550)
            self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
