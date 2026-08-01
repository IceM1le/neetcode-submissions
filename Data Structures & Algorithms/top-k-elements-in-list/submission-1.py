class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1            
        buckets = [[] for _ in range(len(nums) + 1)]
        for i, v in freq_dict.items():
            buckets[v].append(i)
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
            if len(result) == k:
                return result
        return result
            