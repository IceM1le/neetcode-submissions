class Solution:
    def isHappy(self, n: int) -> bool:
        set_nums = set()
        while n != 1 and n not in set_nums:
            set_nums.add(n)
            sum_digits = 0
            while n > 0:
                n, digit = divmod(n, 10)
                sum_digits += pow(digit, 2)
            n = sum_digits
        return n == 1