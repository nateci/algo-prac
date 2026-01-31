class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = []

        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.append(nums[i])
            else:
                seen.remove(nums[i])
        return seen.pop()
                        