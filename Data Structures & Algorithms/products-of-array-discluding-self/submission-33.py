class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product, zerocnt = 1, 0
        res = [0] * n

        for num in nums:
            if num:
                product *= num
            else:
                zerocnt +=1
        
        if zerocnt > 1:
            return res
        
        for i in range(n):
            if zerocnt:
                if nums[i]:
                    res[i] = 0
                else:
                    res[i] = product
            else:
                res[i] = product // nums[i]
        
        return res





             
