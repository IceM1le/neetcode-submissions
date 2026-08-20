class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        from collections import Counter
        count = Counter(hand)
        for card in sorted(hand):
            freq = count[card]
            if freq > 0:
                for i in range(groupSize):
                    if count[card + i] < freq: return False
                    count[card + i] -= 1
        return True
