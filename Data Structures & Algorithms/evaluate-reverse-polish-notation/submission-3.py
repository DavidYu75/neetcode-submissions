class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '-':
                second_number = stack.pop()
                first_number = stack.pop()
                stack.append(first_number - second_number)
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                second_number = stack.pop()
                first_number = stack.pop()
                stack.append(int(float(first_number) / second_number))
            else:
                stack.append(int(token))
            
        return stack[-1]