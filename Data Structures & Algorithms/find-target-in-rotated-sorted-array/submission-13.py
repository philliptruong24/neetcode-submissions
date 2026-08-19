class Solution:
    def search(self, nums: List[int], target: int) -> int:
    
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] <= nums[-1]:
                r = mid
            else:
                l = mid + 1

        
        pivot = l
        if nums[pivot] <= target and target <= nums[len(nums) - 1]:
            l = pivot
            r = len(nums) - 1
        else:
            l = 0
            r = pivot

        while l < r:
                mid = l + (r - l) // 2
                if nums[mid] >= target:
                    r = mid
                else:
                    l = mid + 1
        
        return l if nums[l] == target else -1