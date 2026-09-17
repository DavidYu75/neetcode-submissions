class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = i
        
        # [3, 4, 5, 6]
        # hashmap = {3: 0, 4: 1, 5: 2, 6: 3}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        
        return []
