class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums:
            return res

        start = end = nums[0]

        for n in nums[1:]:
            if n == end + 1:
                end = n

            else:
                if start == end:
                    res.append(str(start))
                else:
                    res.append(str(start) + "->" + str(end))
                start = end = n

        if start == end:
            res.append(str(start))

        else:
            res.append(str(start) + "->" + str(end))

        return res
