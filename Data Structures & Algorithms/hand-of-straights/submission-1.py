class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        from collections import Counter
        
        count = Counter(hand)
        
        for card in sorted(hand):
            if count[card] > 0:
                freq = count[card]
                for i in range(groupSize):
                    if count[card + i] < freq:
                        return False
                    count[card + i] -= freq
        
        return True