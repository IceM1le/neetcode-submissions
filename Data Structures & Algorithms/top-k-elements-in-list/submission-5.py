class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq_dict = {}
        for i in range(n):
            freq_dict[nums[i]] = freq_dict.get(nums[i], 0) + 1
        buckets = [[] for _ in range(n + 1)]
        for i, freq in freq_dict.items():
            buckets[freq].append(i)
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
            if len(result) == k:
                return result
        return result