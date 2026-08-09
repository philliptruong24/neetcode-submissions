class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        largest = 0
        while l < r:
            size = (r - l) * min(heights[l], heights[r])
            largest = max(largest, size)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -=1
        
        return largest