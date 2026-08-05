class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_parentheses = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in dict_parentheses:
                if stack and stack.pop() == dict_parentheses[c]: 
                   pass        
                else:
                    return False
            else:
                stack.append(c)
        return False if stack else True