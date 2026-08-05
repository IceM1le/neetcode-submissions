class Solution:
    def evalRPN(self, tokens: List[str]) -> int:        
        if not tokens: return 0                
        stack = []
        for i in range(len(tokens)):
            token = tokens[i]
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                stack.append(- stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                stack.append(int(1 / stack.pop() * stack.pop()))            
            else:
                stack.append(int(token))
        return stack[-1]