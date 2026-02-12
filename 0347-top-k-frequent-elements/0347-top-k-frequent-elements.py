import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        heap = []
        result = []
        for key, freq in count.items():
            heapq.heappush(heap, (-freq, key))

        while len(result) < k:
            result.append(heapq.heappop(heap)[1])


        return result
        



        