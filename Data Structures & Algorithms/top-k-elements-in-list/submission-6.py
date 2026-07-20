class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = {}
        for num in nums:
            freqmap[num] = freqmap.get(num, 0) + 1
        max_heap = []
        for key in freqmap:
            max_heap.append([-freqmap[key],key])
        
        heapq.heapify(max_heap)
        result = []
        for _ in range(k):
            freq, key = heapq.heappop(max_heap)
            result.append(key)
        
        return result

