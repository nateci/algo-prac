class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        cur_length = 1
        max_length = 0

        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                cur_length += 1
            else:
                max_length = max(cur_length, max_length)
                cur_length = 1

        max_length = max(cur_length, max_length)
        return max_length
