class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        stack = []
        for c in s:
            if c in parentheses:
                if not stack or stack[-1] != parentheses[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0