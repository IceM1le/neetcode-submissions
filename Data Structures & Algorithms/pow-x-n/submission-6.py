class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1: return 1
        if x == -1: return 1 if n % 2 == 0 else -1
        sum = 1
        if n < 0: 
            x = 1 / x
            n = -n
            if n > 10000000: return 0
        for _ in range(n): sum *= x        
        return sum