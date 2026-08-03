class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        largest = 0
        while l < r:
            curr = (r - l) * min(heights[r], heights[l])
            largest = max(largest, curr)

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return largest

