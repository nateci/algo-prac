class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix) - 1
        while top <= bot:
            mid = (top + bot) // 2

            if matrix[mid][0] < target < matrix[mid][-1]:
                break
            elif matrix[mid][0] < target:
                top = mid + 1
            else:
                bot = mid - 1
        
        row = (bot + top) // 2
        right = len(matrix[row]) - 1
        left = 0

        while left <= right:
            mid = (left + right) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False