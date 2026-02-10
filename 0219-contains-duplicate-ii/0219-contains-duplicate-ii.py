class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen:
                distance = i - seen[nums[i]]
                if distance <= k:
                    return True

                else:
                    seen[nums[i]] = i

            else:
                seen[nums[i]] = i

        return False