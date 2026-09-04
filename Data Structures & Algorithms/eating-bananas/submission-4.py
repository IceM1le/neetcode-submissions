class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        res = right = max(piles)
        while left <= right:
            k = (left + right) // 2
            cur_h = 0
            for p in piles:
                cur_h += -(-p // k)
            if cur_h > h:
                left = k + 1
            else:
                res = min(k, res)
                right = k - 1
        return res