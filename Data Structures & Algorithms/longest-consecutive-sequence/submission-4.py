class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for num in num_set:
            if num - 1 in num_set:
                continue
            else:
                current_length = 1
                current_num = num
                while current_num + 1 in num_set:
                    current_length += 1
                    current_num += 1
                max_length = max(max_length, current_length)

        return max_length