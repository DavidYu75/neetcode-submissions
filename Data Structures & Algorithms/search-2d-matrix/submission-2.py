class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_row, last_row = 0, len(matrix) - 1

        target_row = 0

        while first_row <= last_row:
            middle_row = (first_row + last_row) // 2

            if matrix[middle_row][0] <= target <= matrix[middle_row][-1]:
                target_row = middle_row
                break
            elif matrix[middle_row][0] > target:
                last_row = middle_row - 1
            else:
                first_row = middle_row + 1
        
        left, right = 0, len(matrix[target_row]) - 1

        while left <= right:
            middle = (left + right) // 2

            if matrix[target_row][middle] == target:
                return True
            elif matrix[target_row][middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return False