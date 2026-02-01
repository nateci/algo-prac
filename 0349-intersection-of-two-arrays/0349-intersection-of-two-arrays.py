class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set()
        result = set()
        
        for num in nums2:
            seen.add(num)

        for num in nums1:
            if num in seen:
                result.add(num)



        return list(result)