class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        nums.sort()

        def dfs(i, total):
            if total == target:
                res.append(curr.copy())
                return
            
            for idx in range(i, len(nums)):
                if total > target:
                    return
                
                curr.append(nums[idx])
                dfs(idx, total + nums[idx])

                curr.pop()
        dfs(0, 0)
        return res