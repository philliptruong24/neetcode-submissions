class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for idx, point in enumerate(points):

            xdiff = math.pow(point[0], 2)
            ydiff = math.pow(point[1], 2)

            maxheap.append((-math.sqrt(xdiff + ydiff), idx))

        heapq.heapify(maxheap)

        while len(maxheap) > k:
            heapq.heappop(maxheap)
        
        res = []
        while maxheap:
            dist, idx = heapq.heappop(maxheap)
            res.append(points[idx])
        
        return res


