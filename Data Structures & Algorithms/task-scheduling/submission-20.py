class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}

        for task in tasks:
            count[task] = count.get(task, 0) - 1

        heap = list(count.values())
        heapq.heapify(heap)

        q = deque()
        cycles = 0

        while heap or q:
            if not heap and q:
                cycles = q[0][0]

            while q and q[0][0] == cycles:
                timer, freq = q.popleft()
                heapq.heappush(heap, freq)

            if heap:
                freq = heapq.heappop(heap)
                freq += 1

                if freq < 0:
                    q.append((cycles + n + 1, freq))

            cycles += 1

        return cycles