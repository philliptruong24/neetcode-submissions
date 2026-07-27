class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, zero_cnt = 1, 0
        res = [0] * len(nums)

        for num in nums:
            if num:
                product *= num
            else:
                zero_cnt += 1
        
        if zero_cnt > 1:
            return res
        
        for i, elem in enumerate(nums):
            if zero_cnt:
                if elem:
                    res[i] = 0
                else:
                    res[i] = product
            else:
                res[i] = product // elem
        return res
            