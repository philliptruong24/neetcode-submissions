class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            largest = heapq.heappop(heap)
            if largest < heap[0]:
                temp = largest - heap[0]
                heapq.heappop(heap)
                heapq.heappush(heap, temp)
            else:
                heapq.heappop(heap)
        
        return -heap[0] if len(heap) == 1 else 0