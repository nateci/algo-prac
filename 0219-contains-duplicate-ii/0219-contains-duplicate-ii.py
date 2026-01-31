class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        seen = {}
        for i in range(len(nums)):
            current_index = i
            current_val = nums[i]

            if current_val in seen:
                previous_index = seen[current_val]
                distance = current_index - previous_index

                if distance <= k:
                    return True
                else:
                    seen[current_val] = current_index

            else:
                seen[current_val] = current_index
                
        return False
        