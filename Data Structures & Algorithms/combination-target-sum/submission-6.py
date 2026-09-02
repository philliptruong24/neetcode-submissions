class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def dfs(i, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            curr.append(nums[i])
            newTotal = total + nums[i]
            dfs(i, newTotal)
            
            curr.pop()
            dfs(i + 1, total)


            
        dfs(0, 0)
        return res