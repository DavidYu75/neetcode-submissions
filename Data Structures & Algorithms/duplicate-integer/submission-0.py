class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums = set()

        for i in nums:
            if i in set_nums:
                return True
            else:
                set_nums.add(i)

        return False