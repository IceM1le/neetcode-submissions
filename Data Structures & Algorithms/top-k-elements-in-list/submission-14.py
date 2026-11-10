class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        n = len(nums)
        bucket = [[] for _ in range(n + 1)]
        res = []
        for num, frq in freq.items():
            bucket[frq].append(num)
        for b in bucket[::-1]:
            if b:
                for num in b:
                    res.append(num)
                if len(res) == k:
                    break
        return res
                