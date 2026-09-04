class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles: return 0
        left = 1
        res = right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            cur = 0
            for p in piles: cur -= -p // mid
            if cur > h: left = mid + 1
            else:
                right = mid - 1
                res = min(res, mid)
        return res