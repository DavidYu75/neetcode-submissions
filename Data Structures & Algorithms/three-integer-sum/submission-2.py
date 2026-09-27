class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)  #O(nlogn)

        result = []

        for i in range(len(sorted_nums)):   # O(n)
            if sorted_nums[i] > 0:
                break
            
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            
            left, right = i + 1, len(sorted_nums) - 1

            while left < right: # O(n - 1)
                curr_sum = sorted_nums[left] + sorted_nums[right]

                if curr_sum + sorted_nums[i] > 0:
                    right -= 1
                elif curr_sum + sorted_nums[i] < 0:
                    left += 1
                else:
                    result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1

                    while sorted_nums[left] == sorted_nums[left - 1] and left < right:
                        left += 1
        
        return result

        # time: O(n^2)
        # space: O(n)
