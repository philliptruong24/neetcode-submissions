class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x, y in points:
            diff = x * x + y * y
            heapq.heappush(minheap, [-diff, x, y])
            if len(minheap) > k:
                heapq.heappop(minheap)
            

        res = []
        while minheap:
            diff, x, y = heapq.heappop(minheap)
            res.append([x,y])
        
        return res
