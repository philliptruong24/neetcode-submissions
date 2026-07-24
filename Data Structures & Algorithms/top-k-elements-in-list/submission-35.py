class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = {}
        for num in nums:
            freqmap[num] = 1 + freqmap.get(num, 0)
        
        heap = []
        for num, freq in freqmap.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
        
        

        

        
    
        
