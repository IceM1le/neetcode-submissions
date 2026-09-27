class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right        
        while left < right:
            mid = (left + right) // 2
            cur = 0
            for p in piles:
                cur -= -p // mid
            if cur > h:
                left = mid + 1
            else:
                right = mid
                res = min(res, mid)
        return res