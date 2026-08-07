class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        while left <= right:
            k = (left + right) // 2
            cur_h = 0
            for p in piles:
                cur_h += -(-(p / k) // 1)
            if cur_h > h:
                left = k + 1
            else:
                res = min(k, res)
                right = k - 1
        return res