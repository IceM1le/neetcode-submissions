class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0    # минимум открытых скобок
        high = 0   # максимум открытых скобок
        
        for c in s:
            if c == '(':
                low += 1
                high += 1
            elif c == ')':
                low -= 1
                high -= 1
            else:  # '*'
                low -= 1    # звёздочка как ')'
                high += 1   # звёздочка как '('
            
            if high < 0:    # слишком много ')'
                return False
            
            low = max(low, 0)  # не может быть отрицательным
        
        return low == 0