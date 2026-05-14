class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # low, high = 0, len(nums) - 1

        # while low <= high:
        #     mid = low + (high - low) // 2
        #     if target == nums[mid]:
        #         return mid
        #     elif target > nums[mid]:
        #         low = mid + 1
        #     else:
        #         high = mid - 1
        
        # return -1

        low, high = 0, len(nums)
        while low < high:
            mid = low + (high - low) // 2
            if target > nums[mid]:
                low = mid + 1
            elif target <= nums[mid]:
                high = mid

        
        return low if low < len(nums) and nums[low] == target else -1


        