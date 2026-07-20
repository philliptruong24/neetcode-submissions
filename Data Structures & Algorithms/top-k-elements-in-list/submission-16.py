class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        heap = []
        for num in count:
            heapq.heappush(heap,(count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result

