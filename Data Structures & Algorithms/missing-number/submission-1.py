class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = set()
        for num in nums:
            res.add(num)
        for i in range(len(nums) + 1):
            if i not in res:
                return i
