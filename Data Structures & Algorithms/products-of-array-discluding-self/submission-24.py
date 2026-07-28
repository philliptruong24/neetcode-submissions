class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, zerocnt = 1, 0
        for num in nums:
            if num:
                product *= num
            else:
                zerocnt += 1
        
        res = [0] * len(nums)
        if zerocnt > 1:
            return res

        for i, num in enumerate(nums):
            if zerocnt:
                if num:
                    res[i] = 0
                else:
                    res[i] = product
            else:
                res[i] = product // num
        

        return res