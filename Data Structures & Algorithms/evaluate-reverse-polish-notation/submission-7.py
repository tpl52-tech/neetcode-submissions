class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {"+", "-", "*", "/"}
        
        for i in range (len(tokens)):
            c = tokens[i]
            if c in operands: 
                a = stack.pop()
                b = stack.pop()
                if c == "+": 
                    stack.append(a + b)
                elif c == "-":
                    stack.append(a - b)
                elif c == "*":
                    stack.append(a * b)
                elif c == "/": 
                    stack.append(a / b)
            else: 
                stack.append(int(c))
        
        return stack.pop()



