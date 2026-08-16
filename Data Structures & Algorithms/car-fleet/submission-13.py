class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        
        pairs.sort()
        times = []
        for i, pair in enumerate(pairs):
            times.append((target - pair[0]) / pair[1])
        
        stack = []

        for i, time in enumerate(times):
            while stack and time >= stack[-1]:
                stack.pop()

            stack.append(time)

        return len(stack)
