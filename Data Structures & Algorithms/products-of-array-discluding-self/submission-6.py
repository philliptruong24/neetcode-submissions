class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, zero_cnt = 1, 0
        res = [0] * len(nums)

        for num in nums:
            if num == 0:
                zero_cnt += 1
            else:
                product *= num
        
        if zero_cnt <= 1:
            for i in range(len(nums)):
                if zero_cnt:
                    if nums[i]:
                        res[i] = 0
                    else:
                        res[i] = product
                else:
                    res[i] = product // nums[i]
        return res
            