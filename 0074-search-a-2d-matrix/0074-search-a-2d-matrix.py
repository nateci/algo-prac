class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix) -1

        while bot >= top:
            mid = (top + bot) // 2

            if matrix[mid][0] <= target and target <= matrix[mid][-1]:
                break

            if matrix[mid][0] < target:
                top = mid + 1

            else:
                bot = mid -1

        row = (top + bot) // 2
        left = 0
        right = len(matrix[row]) - 1


        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True

            if  matrix[row][mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return False

        