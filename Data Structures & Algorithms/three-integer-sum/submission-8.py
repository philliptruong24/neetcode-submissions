class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        res = []
        while i < len(nums) - 2:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue 

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -=1
                else:
                    res.append([nums[i], nums[j], nums[k]])

                    left_val = nums[k]
                    right_val = nums[k]

                    while j < k and nums[j] == left_val:
                        j += 1
                    
                    while j < k and nums[k] == right_val:
                        k -= 1
        
            i += 1
        return res


