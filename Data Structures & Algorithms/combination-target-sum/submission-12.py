class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        curr = []

        def dfs(i, total):
            if total == target:
                res.append(curr.copy())
                return
            
            for j in range(i, len(nums)):
                if total > target:
                    return
                
                curr.append(nums[j])
                dfs(j, total + nums[j])

                curr.pop()
        
        dfs(0, 0)
        return res