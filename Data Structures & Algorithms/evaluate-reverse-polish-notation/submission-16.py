class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:            
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                stack.append(- stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                stack.append(int((stack.pop() ** -1) * stack.pop()))
            else:
                stack.append(int(token))
        return stack.pop()