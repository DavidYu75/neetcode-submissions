class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        position = n - 1

        while left <= right:
            if (nums[left] * nums[left]) > (nums[right] * nums[right]):
                result[position] = nums[left] * nums[left]
                left += 1
            else:
                result[position] = nums[right] * nums[right]
                right -= 1
            
            position -= 1
        
        return result