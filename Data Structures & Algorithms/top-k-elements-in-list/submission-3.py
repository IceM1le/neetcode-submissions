class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = dict()
        n = len(nums)
        for i in range(n):
            freq_dict[nums[i]] = freq_dict.get(nums[i], 0) + 1
        buckets = [[] for i in range(n + 1)]
        for val, freq in freq_dict.items():
            buckets[freq].append(val)
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result            
        return result