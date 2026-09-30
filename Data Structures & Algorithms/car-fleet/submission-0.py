class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = []

        for i in range(len(position)):
            position_speed.append((position[i], speed[i]))
        
        position_speed.sort()

        stack = []

        for i in range(len(position_speed) - 1, -1, -1):
            current_time = (target - position_speed[i][0]) / position_speed[i][1]
            stack.append(current_time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
                