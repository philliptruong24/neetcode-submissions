class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # low, high = 0, len(nums) - 1

        # while low <= high:
        #     mid = low + (high - low) // 2
        #     if target == nums[mid]:
        #         return mid
        #     elif target < nums[mid]:
        #         high = mid - 1
        #     else:
        #         low = mid + 1

        # return -1

        low, high = 0, len(nums)
        while low < high:
            mid = low + (high - low) // 2

            if nums[mid] > target:
                high = mid
            else:
                low = mid + 1
        
        return low - 1 if low and nums[low -1 ] == target else -1