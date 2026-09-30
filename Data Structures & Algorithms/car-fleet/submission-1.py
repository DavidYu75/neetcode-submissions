class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = []

        for i in range(len(position)):
            position_speed.append((position[i], speed[i]))

        position_speed.sort(reverse=True)
        stack = []

        for pos, sp in position_speed:
            time = (target - pos) / sp
            stack.append(time)
            
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

        # time: O(nlogn)
        # space: O(n)