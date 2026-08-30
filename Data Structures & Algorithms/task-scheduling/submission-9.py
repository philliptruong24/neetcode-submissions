class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = 0
        count = {}

        # Count remaining tasks using negative frequencies
        for task in tasks:
            count[task] = count.get(task, 0) - 1

        # Available tasks
        maxheap = []

        for task, freq in count.items():
            heapq.heappush(maxheap, (freq, task))

        # (ready_time, task)
        cooldowns = deque()

        while maxheap or cooldowns:

            # If nothing can currently run, skip directly
            # to when the next task becomes available
            if not maxheap and cooldowns:
                res = max(res, cooldowns[0][0])

            # Move finished cooldowns back into available heap
            while cooldowns and cooldowns[0][0] <= res:
                ready_time, task = cooldowns.popleft()
                heapq.heappush(maxheap, (count[task], task))

            # Run the most frequent available task
            if maxheap:
                freq, task = heapq.heappop(maxheap)

                count[task] += 1

                # More copies of this task remain
                if count[task] < 0:
                    cooldowns.append((res + n + 1, task))

            res += 1

        return res
