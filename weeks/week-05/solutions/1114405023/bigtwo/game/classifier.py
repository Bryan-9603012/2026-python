from __future__ import annotations
from enum import IntEnum
from typing import List, Optional, Tuple
from game.models import Card, Hand


class CardType(IntEnum):
    SINGLE = 1
    PAIR = 2
    TRIPLE = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8


class HandClassifier:
    def __init__(self) -> None:
        pass

    def classify(self, cards: List[Card]) -> Optional[Tuple[CardType, int, int]]:
        if not cards:
            return None
        
        n = len(cards)
        
        if n == 1:
            return self._classify_single(cards[0])
        elif n == 2:
            result = self._classify_pair(cards)
            if result:
                return result
            return None
        elif n == 3:
            result = self._classify_triple(cards)
            if result:
                return result
            return None
        elif n == 5:
            return self._classify_five(cards)
        
        return None

    def _classify_single(self, card: Card) -> Tuple[CardType, int, int]:
        return (CardType.SINGLE, card.rank, card.suit)

    def _classify_pair(self, cards: List[Card]) -> Optional[Tuple[CardType, int, int]]:
        if len(cards) == 2 and cards[0].rank == cards[1].rank:
            return (CardType.PAIR, cards[0].rank, min(cards[0].suit, cards[1].suit))
        return None

    def _classify_triple(self, cards: List[Card]) -> Optional[Tuple[CardType, int, int]]:
        if len(cards) == 3 and cards[0].rank == cards[1].rank == cards[2].rank:
            return (CardType.TRIPLE, cards[0].rank, 0)
        return None

    def _classify_five(self, cards: List[Card]) -> Optional[Tuple[CardType, int, int]]:
        ranks = [c.rank for c in cards]
        suits = [c.suit for c in cards]
        sorted_ranks = sorted(ranks)
        
        is_flush = len(set(suits)) == 1
        is_straight = self._is_straight(sorted_ranks)
        
        rank_counts = {}
        for r in ranks:
            rank_counts[r] = rank_counts.get(r, 0) + 1
        
        counts = sorted(rank_counts.values(), reverse=True)
        
        if is_straight and is_flush:
            return (CardType.STRAIGHT_FLUSH, max(ranks), 0)
        elif counts == [4, 1]:
            main_rank = [r for r, c in rank_counts.items() if c == 4][0]
            return (CardType.FOUR_OF_A_KIND, main_rank, 0)
        elif counts == [3, 2]:
            main_rank = [r for r, c in rank_counts.items() if c == 3][0]
            return (CardType.FULL_HOUSE, main_rank, 0)
        elif is_flush:
            return (CardType.FLUSH, max(ranks), suits[0])
        elif is_straight:
            return (CardType.STRAIGHT, max(ranks), 0)
        
        return None

    def _is_straight(self, sorted_ranks: List[int]) -> bool:
        if len(sorted_ranks) != 5:
            return False
        
        unique_ranks = sorted(set(sorted_ranks))
        if len(unique_ranks) != 5:
            return False
        
        if unique_ranks == [3, 4, 5, 14, 15]:
            return True
        
        if unique_ranks == [3, 4, 5, 6, 14]:
            return True
        
        for i in range(1, len(unique_ranks)):
            if unique_ranks[i] - unique_ranks[i-1] != 1:
                return False
        
        return True

    def compare(self, hand1: Optional[Tuple[CardType, int, int]], hand2: Optional[Tuple[CardType, int, int]]) -> int:
        if hand1 is None:
            return -1
        if hand2 is None:
            return 1
        
        type1, rank1, suit1 = hand1
        type2, rank2, suit2 = hand2
        
        if rank1 == 15:
            rank1 = 14.5
        if rank2 == 15:
            rank2 = 14.5
        
        if type1 != type2:
            return 1 if type1 > type2 else -1
        if rank1 != rank2:
            return 1 if rank1 > rank2 else -1
        if suit1 != suit2:
            return 1 if suit1 > suit2 else -1
        
        return 0

    def can_play(self, hand: Optional[Tuple[CardType, int, int]], new_hand, is_first: bool = False) -> bool:
        if is_first:
            if isinstance(new_hand, list):
                return len(new_hand) == 1 and new_hand[0].rank == 3 and new_hand[0].suit == 0
            return False
        
        if hand is None:
            return True
        
        if isinstance(new_hand, (tuple, list)) and len(new_hand) == 3 and isinstance(new_hand[0], CardType):
            new_classified = new_hand
        else:
            new_classified = self.classify(new_hand)
            if new_classified is None:
                return False
        
        return self.compare(new_classified, hand) > 0
