class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] <= nums[r]:
                res = min(res, nums[mid])
                r = mid - 1
            else:
                l = mid + 1
        
        return res

