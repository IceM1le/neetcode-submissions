class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                stack.append(- stack.pop() + stack.pop())
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                val = 1 / stack.pop() * stack.pop()
                if val >= 0:
                    stack.append(int(val // 1))
                else:
                    stack.append(int(-(-val // 1)))
            else:
                stack.append(int(t))
        return stack.pop()        