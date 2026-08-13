class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []
        for token in tokens[:]:
            if token in operators:
                b = int(stack.pop())
                a = int(stack.pop())
                if token == '+':
                    stack.append(str(a + b))
                elif token == '-':
                    stack.append(str(a - b))
                elif token == '*':
                    stack.append(str(a * b))
                elif token == '/':
                    stack.append(str(int(a / b)))
            else:
                stack.append(token)
        return int(stack[0])