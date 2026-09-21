class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1, 2, 4, 6]
        # prefix_products = [1, 1, 2, 8]
        # suffix_products = [48, 24, 6, 1]

        # 1: 2 * 4 * 6 = 48
        # 2: 4 * 6 = 24 1 24 * 1
        # 4: 1 * 2 = 2 6 2 * 6 = 12

        n = len(nums)
        result = [0] * n
        prefix_products = [0] * n
        suffix_products = [0] * n

        prefix_products[0] = 1
        suffix_products[-1] = 1

        for i in range(1, n):
            prefix_products[i] = nums[i - 1] * prefix_products[i - 1]

        for i in range(n - 2, -1, -1):
            suffix_products[i] = nums[i + 1] * suffix_products[i + 1]
        
        for i in range(n):
            result[i] = prefix_products[i] * suffix_products[i]

        return result

        # time: O(n)
        # space: O(n)