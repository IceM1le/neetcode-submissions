class Solution:
    def isValid(self, s: str) -> bool:
        pr = {
            "}": "{", ")": "(", "]": "["
        }
        stack = []
        for c in s:
            if c in pr:
                if stack and stack[-1] == pr[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0