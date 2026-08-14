class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)
        while i < j:
            mid = ((j - i) // 2) + i
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid
            else:
                i = mid + 1
        
        return -1

        