class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles: return 0
        left, right = 1, max(piles)
        res = right
        while left <= right:
            cur = 0
            mid = (left + right) // 2
            for p in piles:
                cur -= -p // mid            
            if cur > h:
                left = mid + 1
            else:
                right = mid - 1
                res = min(res, mid)
        return res