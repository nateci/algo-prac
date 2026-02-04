class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        current_length = 1
        max_length = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            elif nums[i] == nums[i -1] + 1:
                current_length += 1
            else:
                max_length = max(current_length, max_length)
                current_length = 1

        max_length = max(current_length, max_length)
        return max_length