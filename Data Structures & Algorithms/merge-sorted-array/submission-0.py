class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first, second = m - 1, n - 1
        position = m + n - 1

        while second >= 0:
            if first >= 0 and nums1[first] > nums2[second]:
                nums1[position] = nums1[first]
                first -= 1
            else:
                nums1[position] = nums2[second]
                second -= 1

            position -= 1
            