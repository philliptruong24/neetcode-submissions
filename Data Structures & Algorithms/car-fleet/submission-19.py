class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:
            arrival = (target - p) / s
            if not stack or stack[-1] < arrival:
                stack.append(arrival)
            
        return len(stack)