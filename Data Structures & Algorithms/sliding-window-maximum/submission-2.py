class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or len(nums) < k:
            return []
        result = [max(nums[:k])]
        left = 1
        for right in range(k, len(nums)):
            if nums[left - 1] < result[-1]:                
                result.append(max(nums[right], result[-1]))
            else:
                if nums[right] >= result[-1]:
                    result.append(nums[right])
                else:
                    result.append(max(nums[left:right+1]))
            left += 1
        return result