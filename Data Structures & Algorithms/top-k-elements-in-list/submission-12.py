class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        freq = Counter(nums)
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        for val, freq in freq.items():
            buckets[freq].append(val)
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for b in buckets[i]:
                res.append(b)
            if len(res) == k:
                break
        return res
