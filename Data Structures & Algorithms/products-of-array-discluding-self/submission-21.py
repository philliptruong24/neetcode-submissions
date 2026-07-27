class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product, zerocnt = 1, 0
        res = [0] * (len(nums))

        for num in nums:
            if num:
                product *= num
            else:
                zerocnt += 1
        
        if zerocnt > 1:
            return res
        
        for i, c in enumerate(nums):
            if zerocnt:
                if c:
                    res[i] = 0
                else:
                    res[i] = product

            else:
                res[i] = product // c

        return res