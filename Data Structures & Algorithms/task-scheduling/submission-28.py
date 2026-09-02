class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        minHeap = []
        for freq in count.values():
            minHeap.append(-freq)
        
        heapq.heapify(minHeap)
        q = deque()
        cycles = 0
        while minHeap or q:
            if not minHeap:
                cycles = q[0][0]
            while q and q[0][0] == cycles:
                time, freq = q.popleft()
                heapq.heappush(minHeap, freq)
            
            freq = heapq.heappop(minHeap)
            cycles += 1

            if freq < -1:
                q.append(((cycles + n), freq + 1))
        
        return cycles