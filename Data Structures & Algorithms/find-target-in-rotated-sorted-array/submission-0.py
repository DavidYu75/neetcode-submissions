class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        # left to len(nums) - 1 is the range starting from lowest number
        # 0 to left - 1 is the range from pivot to largest number
        # check which range target belongs to
        # then perform binary search on that range

        if nums[left] <= target <= nums[-1]:
            l, r = left, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
        else:
            l, r = 0, left - 1
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1