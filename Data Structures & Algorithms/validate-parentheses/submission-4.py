class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthses = {
            "}": "{", 
            ")": "(",
            "]": "["
        }
        for c in s:
            if c in parenthses:
                if stack and stack[-1] == parenthses[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0