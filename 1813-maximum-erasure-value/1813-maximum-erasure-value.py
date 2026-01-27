class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = left = count = 0
        seen = set()

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                count -= nums[left]
                left += 1

            seen.add(nums[right])
            count += nums[right]

            res = max(count, res)

        return res