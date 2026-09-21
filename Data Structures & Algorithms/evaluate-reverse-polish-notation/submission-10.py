class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens: return 0
        stack = []
        res = 0
        for t in tokens:            
            if t == "+": stack.append(stack.pop() + stack.pop())
            elif t == "-": stack.append(-stack.pop() + stack.pop())
            elif t == "*": stack.append(stack.pop() * stack.pop())
            elif t == "/": 
                cur = 1 / stack.pop() * stack.pop()
                if cur > 0: stack.append(cur // 1)
                else: stack.append(-(-cur // 1))
            else:
                stack.append(int(t))
        return int(stack[-1])