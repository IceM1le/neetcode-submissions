class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left <= right:
            summa = numbers[left] + numbers[right]
            if summa == target: 
                return [left + 1, right + 1]
            elif summa < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]