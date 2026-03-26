from __future__ import annotations
from typing import List, Optional


class Card:
    SUITS = ['♣', '♦', '♥', '♠']
    RANKS = {3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'T', 11: 'J', 12: 'Q', 13: 'K', 14: 'A', 15: '2'}

    def __init__(self, rank: int, suit: int) -> None:
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        return f'{Card.SUITS[self.suit]}{Card.RANKS[self.rank]}'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other: Card) -> bool:
        if self.rank != other.rank:
            return self.rank < other.rank
        return self.suit < other.suit

    def __hash__(self) -> int:
        return hash((self.rank, self.suit))

    def to_sort_key(self) -> tuple[int, int]:
        return (self.rank, self.suit)


class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = self._create_cards()

    def _create_cards(self) -> List[Card]:
        cards = []
        for suit in range(4):
            for rank in range(3, 16):
                cards.append(Card(rank, suit))
        return cards

    def shuffle(self) -> None:
        import random
        random.shuffle(self.cards)

    def deal(self, n: int) -> List[Card]:
        cards = self.cards[:n]
        self.cards = self.cards[n:]
        return cards


class Hand(list):
    def __init__(self, cards: Optional[List[Card]] = None) -> None:
        super().__init__(cards if cards is not None else [])

    def sort_desc(self) -> None:
        self.sort(key=lambda c: (-c.rank, -c.suit))

    def find_3_clubs(self) -> Optional[Card]:
        for card in self:
            if card.rank == 3 and card.suit == 0:
                return card
        return None

    def remove(self, cards: List[Card]) -> None:
        for card in cards:
            if card in self:
                list.remove(self, card)


class Player:
    def __init__(self, name: str, is_ai: bool = False) -> None:
        self.name: str = name
        self.is_ai: bool = is_ai
        self.hand: Hand = Hand()
        self.score: int = 0

    def take_cards(self, cards: List[Card]) -> None:
        self.hand.extend(cards)

    def play_cards(self, cards: List[Card]) -> List[Card]:
        self.hand = Hand([c for c in self.hand if c not in cards])
        return cards
