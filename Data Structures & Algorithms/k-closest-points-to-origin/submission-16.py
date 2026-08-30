class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for idx, (x, y) in enumerate(points):
            diff = x * x + y * y
            heapq.heappush(minheap, (-diff, idx))
            if len(minheap) > k:
                heapq.heappop(minheap)
            

        res = []
        while minheap:
            diff, idx = heapq.heappop(minheap)
            res.append(points[idx])
        
        return res
