from __future__ import annotations
from typing import List, Optional, Set, Tuple
from itertools import combinations
from game.models import Card, Hand
from game.classifier import CardType, HandClassifier


class HandFinder:
    def __init__(self) -> None:
        self.classifier = HandClassifier()

    def find_singles(self, hand: Hand) -> List[List[Card]]:
        return [[card] for card in hand]

    def find_pairs(self, hand: Hand) -> List[List[Card]]:
        result = []
        rank_groups = {}
        for card in hand:
            if card.rank not in rank_groups:
                rank_groups[card.rank] = []
            rank_groups[card.rank].append(card)
        
        for rank, cards in rank_groups.items():
            if len(cards) >= 2:
                for pair in combinations(cards, 2):
                    result.append(list(pair))
        
        return result

    def find_triples(self, hand: Hand) -> List[List[Card]]:
        result = []
        rank_groups = {}
        for card in hand:
            if card.rank not in rank_groups:
                rank_groups[card.rank] = []
            rank_groups[card.rank].append(card)
        
        for rank, cards in rank_groups.items():
            if len(cards) >= 3:
                for triple in combinations(cards, 3):
                    result.append(list(triple))
        
        return result

    def find_straight(self, hand: Hand) -> List[List[Card]]:
        result = []
        rank_groups = {}
        for card in hand:
            if card.rank not in rank_groups:
                rank_groups[card.rank] = []
            rank_groups[card.rank].append(card)
        
        unique_ranks = sorted(rank_groups.keys())
        
        for i in range(len(unique_ranks)):
            for j in range(i + 1, len(unique_ranks) + 1):
                ranks_slice = unique_ranks[i:j]
                if len(ranks_slice) == 5:
                    if self._is_valid_straight(ranks_slice):
                        cards = []
                        for r in ranks_slice:
                            cards.append(rank_groups[r][0])
                        result.append(cards)
        
        return result

    def _is_valid_straight(self, ranks: List[int]) -> bool:
        if len(ranks) != 5:
            return False
        
        unique_ranks = sorted(set(ranks))
        if len(unique_ranks) != 5:
            return False
        
        if unique_ranks == [3, 4, 5, 14, 15]:
            return True
        
        for i in range(1, len(unique_ranks)):
            if unique_ranks[i] - unique_ranks[i-1] != 1:
                return False
        
        return True

    def find_flush(self, hand: Hand) -> List[List[Card]]:
        result = []
        suit_groups = {suit: [] for suit in range(4)}
        for card in hand:
            suit_groups[card.suit].append(card)
        
        for suit, cards in suit_groups.items():
            if len(cards) >= 5:
                for combo in combinations(cards, 5):
                    result.append(list(combo))
        
        return result

    def find_full_house(self, hand: Hand) -> List[List[Card]]:
        result = []
        rank_groups = {}
        for card in hand:
            if card.rank not in rank_groups:
                rank_groups[card.rank] = []
            rank_groups[card.rank].append(card)
        
        triple_ranks = [r for r, cards in rank_groups.items() if len(cards) >= 3]
        pair_ranks = [r for r, cards in rank_groups.items() if len(cards) >= 2]
        
        for triple_rank in triple_ranks:
            for triple in combinations(rank_groups[triple_rank], 3):
                for pair_rank in pair_ranks:
                    if pair_rank == triple_rank:
                        continue
                    for pair in combinations(rank_groups[pair_rank], 2):
                        result.append(list(triple) + list(pair))
        
        return result

    def find_four_of_a_kind(self, hand: Hand) -> List[List[Card]]:
        result = []
        rank_groups = {}
        for card in hand:
            if card.rank not in rank_groups:
                rank_groups[card.rank] = []
            rank_groups[card.rank].append(card)
        
        for rank, cards in rank_groups.items():
            if len(cards) >= 4:
                for four in combinations(cards, 4):
                    remaining = [c for c in hand if c not in four]
                    if remaining:
                        result.append(list(four) + [remaining[0]])
        
        return result

    def find_straight_flush(self, hand: Hand) -> List[List[Card]]:
        result = []
        suit_groups = {suit: [] for suit in range(4)}
        for card in hand:
            suit_groups[card.suit].append(card)
        
        for suit, cards in suit_groups.items():
            if len(cards) >= 5:
                finder = HandFinder()
                for combo in combinations(cards, 5):
                    combo_list = list(combo)
                    if self.classifier.classify(combo_list) == (CardType.STRAIGHT_FLUSH, max(c.rank for c in combo_list), 0):
                        result.append(combo_list)
        
        return result

    def find_valid_plays(self, hand: Hand, last_play: Optional[Tuple[CardType, int, int]], is_first: bool = False) -> List[List[Card]]:
        if is_first:
            clubs_3 = hand.find_3_clubs()
            if clubs_3:
                return [[clubs_3]]
            return []
        
        valid_plays = []
        card_type, last_rank, last_suit = last_play if last_play else (None, None, None)
        
        if card_type == CardType.SINGLE or last_play is None:
            for single in self.find_singles(hand):
                classified = self.classifier.classify(single)
                if classified and self.classifier.compare(classified, last_play) > 0:
                    valid_plays.append(single)
        
        if card_type == CardType.PAIR or last_play is None:
            for pair in self.find_pairs(hand):
                classified = self.classifier.classify(pair)
                if classified and self.classifier.compare(classified, last_play) > 0:
                    valid_plays.append(pair)
        
        if card_type == CardType.TRIPLE or last_play is None:
            for triple in self.find_triples(hand):
                classified = self.classifier.classify(triple)
                if classified and self.classifier.compare(classified, last_play) > 0:
                    valid_plays.append(triple)
        
        if card_type in [CardType.STRAIGHT, CardType.FLUSH, CardType.FULL_HOUSE, CardType.FOUR_OF_A_KIND, CardType.STRAIGHT_FLUSH] or last_play is None:
            for straight in self.find_straight(hand):
                classified = self.classifier.classify(straight)
                if classified and self.classifier.compare(classified, last_play) > 0:
                    valid_plays.append(straight)
            for flush in self.find_flush(hand):
                classified = self.classifier.classify(flush)
                if classified and self.classifier.compare(classified, last_play) > 0:
                    valid_plays.append(flush)
            for fh in self.find_full_house(hand):
                classified = self.classifier.classify(fh)
                if classified and self.classifier.compare(classified, last_play) > 0:
                    valid_plays.append(fh)
            for four in self.find_four_of_a_kind(hand):
                classified = self.classifier.classify(four)
                if classified and self.classifier.compare(classified, last_play) > 0:
                    valid_plays.append(four)
            for sf in self.find_straight_flush(hand):
                classified = self.classifier.classify(sf)
                if classified and self.classifier.compare(classified, last_play) > 0:
                    valid_plays.append(sf)
        
        return valid_plays
