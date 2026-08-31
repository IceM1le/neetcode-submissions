class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        from collections import Counter
        n = len(nums)
        freq = Counter(nums)
        buckets = [[] for _ in range(n + 1)]
        for num, freq in freq.items():
            buckets[freq].append(num)
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for b in buckets[i]:
                res.append(b)
            if len(res) == k: return res