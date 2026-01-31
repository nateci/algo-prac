class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}

        res = majority = 0

        for n in nums:
            count[n] = count.get(n, 0) + 1

            if count[n] > majority:
                res = n
                majority = count[n]

        return res