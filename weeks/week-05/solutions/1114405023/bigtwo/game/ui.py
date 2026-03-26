from __future__ import annotations
import pygame
import sys
from typing import List, Optional, Tuple
from game.models import Card, Hand
from game.game import BigTwoGame


pygame.init()


class CardRenderer:
    CARD_WIDTH = 50
    CARD_HEIGHT = 70
    CARD_BACKGROUND = (255, 255, 255)
    CARD_BORDER = (0, 0, 0)
    SUIT_COLORS = {
        0: (0, 0, 0),
        1: (255, 0, 0),
        2: (255, 0, 0),
        3: (0, 0, 0)
    }
    SUIT_SYMBOLS = ['♣', '♦', '♥', '♠']
    RANK_SYMBOLS = {3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'T', 11: 'J', 12: 'Q', 13: 'K', 14: 'A', 15: '2'}

    @classmethod
    def render(cls, surface: pygame.Surface, card: Card, x: int, y: int) -> None:
        rect = pygame.Rect(x, y, cls.CARD_WIDTH, cls.CARD_HEIGHT)
        pygame.draw.rect(surface, cls.CARD_BACKGROUND, rect)
        pygame.draw.rect(surface, cls.CARD_BORDER, rect, 2)
        
        color = cls.SUIT_COLORS[card.suit]
        font = pygame.font.Font(None, 20)
        rank_text = font.render(cls.RANK_SYMBOLS[card.rank], True, color)
        
        surface.blit(rank_text, (x + 3, y + 3))
        suit_symbol = cls.SUITS_SYMBOLS[card.suit]
        suit_color = (255, 0, 0) if card.suit in [1, 2] else (0, 0, 0)
        suit_render = font.render(suit_symbol, True, suit_color)
        surface.blit(suit_render, (x + 3, y + 20))
        
        center_suit = font.render(cls.SUITS_SYMBOLS[card.suit], True, suit_color)
        sx = x + cls.CARD_WIDTH // 2 - center_suit.get_width() // 2
        sy = y + cls.CARD_HEIGHT // 2 - center_suit.get_height() // 2
        surface.blit(center_suit, (sx, sy))

    @classmethod
    def render_back(cls, surface: pygame.Surface, x: int, y: int) -> None:
        rect = pygame.Rect(x, y, cls.CARD_WIDTH, cls.CARD_HEIGHT)
        pygame.draw.rect(surface, (50, 50, 150), rect)
        pygame.draw.rect(surface, cls.CARD_BORDER, rect, 2)
        
        font = pygame.font.Font(None, 16)
        text = font.render("BT", True, (255, 255, 255))
        surface.blit(text, (x + 15, y + 25))

    @classmethod
    def get_card_rect(cls, x: int, y: int) -> pygame.Rect:
        return pygame.Rect(x, y, cls.CARD_WIDTH, cls.CARD_HEIGHT)


class HandRenderer:
    def __init__(self) -> None:
        self.card_renderer = CardRenderer
        self.selected_cards: List[Card] = []

    def render(self, surface: pygame.Surface, hand: Hand, x: int, y: int, show_face_down: bool = False) -> None:
        card_width = self.card_renderer.CARD_WIDTH
        spacing = 5
        
        for i, card in enumerate(hand):
            card_x = x + i * (card_width + spacing)
            is_selected = card in self.selected_cards
            card_y = y - 15 if is_selected else y
            
            if show_face_down:
                self.card_renderer.render_back(surface, card_x, card_y)
            else:
                self.card_renderer.render(surface, card, card_x, card_y)

    def handle_click(self, pos: Tuple[int, int], hand: Hand, x: int, y: int) -> Optional[Card]:
        card_width = self.card_renderer.CARD_WIDTH
        spacing = 5
        
        for i, card in enumerate(hand):
            card_x = x + i * (card_width + spacing)
            card_y = y - 15 if card in self.selected_cards else y
            rect = self.card_renderer.get_card_rect(card_x, card_y)
            
            if rect.collidepoint(pos):
                if card in self.selected_cards:
                    self.selected_cards.remove(card)
                else:
                    self.selected_cards.append(card)
                return card
        
        return None

    def get_selected(self) -> List[Card]:
        return self.selected_cards.copy()

    def clear_selection(self) -> None:
        self.selected_cards.clear()


class BigTwoUI:
    WINDOW_WIDTH = 900
    WINDOW_HEIGHT = 700
    BUTTON_COLOR = (70, 130, 180)
    TEXT_COLOR = (255, 255, 255)

    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Big Two - 老大老二")
        self.clock = pygame.time.Clock()
        self.game = BigTwoGame()
        self.game.setup()
        self.human_hand_renderer = HandRenderer()
        self.play_button_rect = pygame.Rect(350, 620, 80, 35)
        self.pass_button_rect = pygame.Rect(450, 620, 80, 35)
        self.font = pygame.font.Font(None, 22)
        self.big_font = pygame.font.Font(None, 28)
        self.running = True
        self.last_action = ""

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_click(event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def handle_mouse_click(self, pos: Tuple[int, int]) -> None:
        if self.game.get_current_player().is_ai:
            return
        
        player = self.game.players[0]
        
        clicked_card = self.human_hand_renderer.handle_click(pos, player.hand, 80, 550)
        
        if self.play_button_rect.collidepoint(pos):
            selected = self.human_hand_renderer.get_selected()
            if selected:
                if self.game.play(selected):
                    self.last_action = f"You played {len(selected)} card(s)"
                    self.human_hand_renderer.clear_selection()
                    self.game.next_turn()
                    self.ai_turn()
                else:
                    self.last_action = "Invalid play!"
            else:
                self.last_action = "Select cards first!"
        elif self.pass_button_rect.collidepoint(pos):
            if self.game.pass_turn():
                self.last_action = "You passed"
                self.game.next_turn()
                self.ai_turn()
            else:
                self.last_action = "Cannot pass now!"

    def ai_turn(self) -> None:
        while self.game.get_current_player().is_ai and not self.game.is_game_over:
            cards = self.game.ai_turn()
            if cards:
                self.last_action = f"{self.game.get_current_player().name} played {len(cards)} card(s)"
            else:
                self.last_action = f"{self.game.get_current_player().name} passed"
            self.game.next_turn()
            pygame.time.delay(500)

    def render_card_row(self, x: int, y: int, count: int, show_back: bool = True) -> None:
        card_width = self.card_renderer.CARD_WIDTH
        spacing = 5
        for i in range(count):
            card_x = x + i * (card_width + spacing)
            if show_back:
                self.card_renderer.render_back(self.screen, card_x, y)

    def render(self) -> None:
        self.screen.fill((0, 100, 0))
        
        pygame.draw.rect(self.screen, (0, 60, 0), (0, 0, 900, 40))
        
        title = self.big_font.render("Big Two - 老大老二", True, (255, 255, 0))
        self.screen.blit(title, (350, 8))
        
        positions = [
            (400, 60, 1),
            (750, 200, 2),
            (400, 340, 3),
            (50, 200, 0)
        ]
        
        for x, y, i in positions:
            player = self.game.players[i]
            is_current = (i == self.game.current_player)
            is_human = (i == 0)
            
            if is_current:
                pygame.draw.rect(self.screen, (255, 255, 0), (x - 60, y - 5, 520, 90), 3)
            
            name_color = (255, 255, 0) if is_current else self.TEXT_COLOR
            name_text = self.big_font.render(f"{player.name}", True, name_color)
            self.screen.blit(name_text, (x, y))
            
            count_text = self.font.render(f"Cards: {len(player.hand)}", True, name_color)
            self.screen.blit(count_text, (x, y + 25))
            
            if is_human:
                self.human_hand_renderer.render(self.screen, player.hand, x, y + 50)
            else:
                self.render_card_row(x, y + 50, len(player.hand))
        
        if self.game.last_play:
            last_type, last_rank, last_suit = self.game.last_play
            type_names = {1: "單張", 2: "對子", 3: "三條", 4: "順子", 5: "同花", 6: "葫蘆", 7: "四條", 8: "同花順"}
            if last_player_idx >= 0:
                last_player_name = self.game.players[self.game.last_player].name
                info_text = f"{last_player_name}: {type_names.get(last_type, 'Unknown')}"
            else:
                info_text = f"Last: {type_names.get(last_type, 'Unknown')}"
        else:
            info_text = "No last play"
        
        last_text = self.font.render(info_text, True, (255, 255, 255))
        self.screen.blit(last_text, (10, 45))
        
        pass_info = f"Pass count: {self.game.pass_count}/3"
        pass_text = self.font.render(pass_info, True, (255, 255, 255))
        self.screen.blit(pass_text, (750, 45))
        
        action_text = self.font.render(self.last_action, True, (255, 255, 0))
        self.screen.blit(action_text, (10, 520))
        
        if len(self.game.players[0].hand) <= 13:
            pygame.draw.rect(self.screen, (255, 255, 255), (340, 610, 200, 55), 0)
        
        pygame.draw.rect(self.screen, self.BUTTON_COLOR, self.play_button_rect)
        play_text = self.font.render("出牌", True, self.TEXT_COLOR)
        self.screen.blit(play_text, (self.play_button_rect.x + 20, self.play_button_rect.y + 8))
        
        pygame.draw.rect(self.screen, (150, 150, 150), self.pass_button_rect)
        pass_text = self.font.render("跳過", True, self.TEXT_COLOR)
        self.screen.blit(pass_text, (self.pass_button_rect.x + 20, self.pass_button_rect.y + 8))
        
        if self.game.is_game_over:
            pygame.draw.rect(self.screen, (0, 0, 0), (300, 280, 300, 150))
            pygame.draw.rect(self.screen, (255, 215, 0), (300, 280, 300, 150), 5)
            winner = self.game.get_winner()
            if winner:
                text = self.big_font.render(f"Winner: {winner.name}!", True, (255, 215, 0))
                self.screen.blit(text, (320, 310))
            
            restart_text = self.font.render("Press ESC to quit", True, (255, 255, 255))
            self.screen.blit(restart_text, (350, 370))

    def run(self) -> None:
        while self.running:
            self.handle_events()
            self.render()
            pygame.display.flip()
            self.clock.tick(30)
        
        pygame.quit()
        sys.exit()


def main() -> None:
    ui = BigTwoUI()
    ui.run()


if __name__ == "__main__":
    main()
