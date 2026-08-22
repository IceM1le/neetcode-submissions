class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        from collections import Counter
        freq_cards = Counter(hand)        
        for card in sorted(hand):
            freq = freq_cards[card]
            for i in range(groupSize):
                if freq > freq_cards[card + i]:
                    return False
                freq_cards[card + i] -= freq
        return True