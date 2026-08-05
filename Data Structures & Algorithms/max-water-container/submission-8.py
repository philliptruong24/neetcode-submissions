class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        largest = 0

        while l < r:
            curr = (r - l) * min(heights[l], heights[r])
            largest = max(largest, curr)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -=1
        return largest


