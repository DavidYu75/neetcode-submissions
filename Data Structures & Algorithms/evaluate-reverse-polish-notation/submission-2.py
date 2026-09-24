class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {'+', '-', '*', '/'}

        stack = []

        for i in range(len(tokens)):
            if tokens[i] in operations:
                second_number = stack.pop()
                first_number = stack.pop()
                result = 0
                
                if tokens[i] == '+':
                    result = first_number + second_number
                elif tokens[i] == '-':
                    result = first_number - second_number
                elif tokens[i] == '*':
                    result = first_number * second_number
                else:
                    result = int(float(first_number) / second_number)
                stack.append(result)
            else:
                stack.append(int(tokens[i]))
        
        return stack[-1]
                