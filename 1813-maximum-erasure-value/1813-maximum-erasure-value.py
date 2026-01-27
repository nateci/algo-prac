class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        cur_sum = 0
        seen = set()
        left = 0

        for i in range(len(nums)):
            while nums[i] in seen:
                seen.remove(nums[left])
                cur_sum -= nums[left]
                left += 1
            seen.add(nums[i])
            cur_sum += nums[i]

            res = max(cur_sum, res)

        return res