class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for i, (x, y) in enumerate(points):
            dist = x * x + y * y
            heapq.heappush(maxHeap, (-dist, i))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        res = []

        while maxHeap:
            dist, i = heapq.heappop(maxHeap)
            res.append(points[i])

        return res


