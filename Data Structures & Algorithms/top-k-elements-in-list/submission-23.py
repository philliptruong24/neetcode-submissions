class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        freq = []
        for n, c in count.items():
            heapq.heappush(freq, (c, n))
            if len(freq) > k:
                heapq.heappop(freq)
            
        res = []
        for i in range(k):
            res.append(heapq.heappop(freq)[1])
        
        return res

        
    
        
