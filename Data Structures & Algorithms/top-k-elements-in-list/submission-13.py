class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        freq = Counter(nums)
        res = []
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        for num, frq in freq.items():
            buckets[frq].append(num)
        for i in range(len(buckets) - 1, -1, -1):
            for b in buckets[i]:
                res.append(b)
            if len(res) == k:
                break
        return res