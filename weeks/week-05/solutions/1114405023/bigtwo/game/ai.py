from __future__ import annotations
from typing import List, Optional, Tuple
from game.models import Card, Hand
from game.classifier import CardType, HandClassifier
from game.finder import HandFinder


class AIStrategy:
    def __init__(self) -> None:
        self.classifier = HandClassifier()
        self.finder = HandFinder()

    def score_hand(self, cards: List[Card], hand: Hand) -> int:
        if not cards:
            return 0
        
        classified = self.classifier.classify(cards)
        if classified is None:
            return 0
        
        card_type, rank, suit = classified
        base_score = int(card_type) * 100
        rank_score = rank * 10
        suit_score = suit
        
        if len(hand) == 1:
            base_score += 10000
        elif len(hand) == 2:
            base_score += 500
        
        spade_bonus = sum(5 for c in cards if c.suit == 3)
        
        return base_score + rank_score + suit_score + spade_bonus

    def select_best(self, hand: Hand, valid_plays: List[List[Card]], is_first: bool = False) -> Optional[List[Card]]:
        if not valid_plays:
            return None
        
        if is_first:
            for play in valid_plays:
                if len(play) == 1 and play[0].rank == 3 and play[0].suit == 0:
                    return play
            return None
        
        scored_plays = []
        for play in valid_plays:
            score = self.score_hand(play, hand)
            remaining_hand = Hand([c for c in hand if c not in play])
            remaining_score = self.score_hand(play, remaining_hand)
            total_score = score + remaining_score
            scored_plays.append((total_score, play))
        
        scored_plays.sort(key=lambda x: -x[0])
        return scored_plays[0][1] if scored_plays else None

    def choose_play(self, hand: Hand, last_play: Optional[Tuple[CardType, int, int]], is_first: bool = False) -> Optional[List[Card]]:
        valid_plays = self.finder.find_valid_plays(hand, last_play, is_first)
        
        if not valid_plays:
            return None
        
        if is_first:
            return self.select_best(hand, valid_plays, is_first=True)
        
        return self.select_best(hand, valid_plays, is_first=False)
