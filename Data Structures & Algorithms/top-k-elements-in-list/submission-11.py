class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        n = len(nums)
        from collections import Counter
        freq = Counter(nums)
        buckets = [[] for i in range(n + 1)]
        for val, freq in freq.items():
            buckets[freq].append(val)
        res = []
        for i in range(n, 0, -1):
            for b in buckets[i]:
                res.append(b)
            if len(res) == k: return res