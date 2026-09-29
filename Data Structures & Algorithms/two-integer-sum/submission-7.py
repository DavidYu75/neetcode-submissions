class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}

        for i in range(len(nums)):
            num_index[nums[i]] = i
        
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in num_index and num_index[complement] != i:
                return [i, num_index[complement]]

        return []