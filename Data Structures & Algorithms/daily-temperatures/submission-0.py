class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_idx = stack.pop()
                result[stack_idx] = idx - stack_idx
            stack.append((temp, idx))
        
        return result

        # time: O(n)
        # space: O(n)