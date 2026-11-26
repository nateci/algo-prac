class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for index,number in enumerate(nums):
            complement = target - number

            if complement in seen:
                return [seen[complement], index]

            
            seen[number] = index

            