class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr = nums
        if not arr:  # Обработка пустого массива
            return 0
        
        # Инициализируем обе переменные первым элементом
        max_ending_here = max_so_far = arr[0]
        
        # Проходим по массиву начиная со второго элемента
        for num in arr[1:]:
            # Обновляем максимальную сумму подмассива, заканчивающегося здесь
            max_ending_here = max(num, max_ending_here + num)
            # Обновляем глобальный максимум
            max_so_far = max(max_so_far, max_ending_here)
        
        return max_so_far