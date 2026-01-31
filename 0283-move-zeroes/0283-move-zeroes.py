class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0

        for fast in range(len(nums)):
            """
            0 1 0 3 12
            s f 
            1 0 0 3 12
              s f
            """
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1

        