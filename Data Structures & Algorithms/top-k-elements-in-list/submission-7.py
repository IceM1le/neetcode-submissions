class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        n = len(nums)
        freq_dict = defaultdict(int)
        for num in nums: freq_dict[num] += 1
        buckets = [[] for _ in range(n + 1)]
        for i, freq in freq_dict.items():
            buckets[freq].append(i)
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]: res.append(num)
            if len(res) == k: return res
        return res
