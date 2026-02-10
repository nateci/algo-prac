class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for x, freq in count.items():
            if freq == 1:
                return x
        
        return -1