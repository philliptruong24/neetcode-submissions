class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                currtemp, curri = stack.pop()
                res[curri] = i - curri
            
            stack.append((temp, i))
        
        return res