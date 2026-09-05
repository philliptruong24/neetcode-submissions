class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(idx):
            if idx == len(nums):
                res.append(nums.copy())
                return
            
            for j in range(idx, len(nums)):
                nums[idx], nums[j] = nums[j], nums[idx]
                dfs(idx + 1)
                nums[idx], nums[j] = nums[j], nums[idx]
        

        dfs(0)

        return res


