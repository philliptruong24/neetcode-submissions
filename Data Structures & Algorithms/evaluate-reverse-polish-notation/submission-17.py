class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []
        for token in tokens:
            if token in operators:
                b = int(stack.pop())
                a = int(stack.pop())
                if token == '+':
                    stack.append(int(a + b))
                elif token == '-':
                    stack.append(int(a - b))
                elif token == '*':
                    stack.append(int(a * b))
                elif token == '/':
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]