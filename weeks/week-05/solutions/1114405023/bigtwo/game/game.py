from __future__ import annotations
from typing import List, Optional, Tuple
from game.models import Card, Deck, Player
from game.classifier import CardType, HandClassifier
from game.finder import HandFinder
from game.ai import AIStrategy


class BigTwoGame:
    def __init__(self) -> None:
        self.players: List[Player] = []
        self.current_player: int = 0
        self.last_play: Optional[Tuple[CardType, int, int]] = None
        self.last_player: int = -1
        self.pass_count: int = 0
        self.is_game_over: bool = False
        self.winner: Optional[Player] = None
        self.classifier = HandClassifier()
        self.finder = HandFinder()
        self.ai = AIStrategy()

    def setup(self) -> None:
        deck = Deck()
        deck.shuffle()
        
        self.players = [
            Player("Player 1", False),
            Player("AI 1", True),
            Player("AI 2", True),
            Player("AI 3", True)
        ]
        
        for i in range(52):
            card = deck.deal(1)[0]
            self.players[i % 4].take_cards([card])
        
        for player in self.players:
            player.hand.sort_desc()
        
        clubs_3_player = -1
        for i, player in enumerate(self.players):
            if player.hand.find_3_clubs():
                clubs_3_player = i
                break
        
        self.current_player = clubs_3_player
        self.last_play = None
        self.last_player = -1
        self.pass_count = 0
        self.is_game_over = False
        self.winner = None

    def get_current_player(self) -> Player:
        return self.players[self.current_player]

    def can_play(self, cards: List[Card]) -> bool:
        player = self.get_current_player()
        for card in cards:
            if card not in player.hand:
                return False
        
        is_first = self.last_play is None and self.pass_count == 0
        classified = self.classifier.classify(cards)
        
        if classified is None:
            return False
        
        return self.classifier.can_play(self.last_play, cards, is_first=is_first)

    def play(self, cards: List[Card]) -> bool:
        if not self.can_play(cards):
            return False
        
        player = self.get_current_player()
        player.hand.remove(cards)
        
        self.last_play = self.classifier.classify(cards)
        self.last_player = self.current_player
        self.pass_count = 0
        
        if len(player.hand) == 0:
            self.is_game_over = True
            self.winner = player
        
        return True

    def pass_turn(self) -> bool:
        if self.last_play is None:
            return False
        
        self.pass_count += 1
        
        if self.pass_count >= 3:
            self.last_play = None
            self.last_player = -1
            self.pass_count = 0
        
        return True

    def next_turn(self) -> None:
        self.current_player = (self.current_player + 1) % 4

    def ai_turn(self) -> Optional[List[Card]]:
        player = self.get_current_player()
        if not player.is_ai:
            return None
        
        is_first = self.last_play is None and self.pass_count == 0
        cards = self.ai.choose_play(player.hand, self.last_play, is_first)
        
        if cards:
            self.play(cards)
        
        return cards

    def get_winner(self) -> Optional[Player]:
        return self.winner

    def get_last_play_info(self) -> Optional[Tuple[CardType, int, int]]:
        return self.last_play
