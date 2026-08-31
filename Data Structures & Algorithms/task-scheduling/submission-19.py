class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            count[task] = count.get(task, 0) - 1
        
        heap = []
        for task, freq in count.items():
            heapq.heappush(heap, (freq, task))
        
        q = deque()
        cycles = 0

        while heap or q:
            while q and q[0][0] == cycles:
                timer, freq, task = q.popleft()
                heapq.heappush(heap, (freq, task))
            if heap:
                freq, task = heapq.heappop(heap)

                if freq + 1 !=  0:
                    q.append((cycles + n + 1 ,freq + 1, task))

            cycles += 1
            
        
        return cycles