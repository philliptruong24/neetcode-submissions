class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()
        while maxHeap or q:
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
            

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
            
                if cnt:
                    q.append([cnt, time + n + 1])
            
            time += 1
        
        return time
