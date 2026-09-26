class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_index = {}

        for i in range(len(nums)):
            number_index[nums[i]] = i
        
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in number_index and i != number_index[complement]:
                return [i, number_index[complement]]
        
        return []