class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        binary search

        [1,3,5,6] target = 5
        """

        left = 0
        right = len(nums)


        while left < right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid


            if nums[mid] > target:
                right -= 1

            else:
                left += 1

        return left