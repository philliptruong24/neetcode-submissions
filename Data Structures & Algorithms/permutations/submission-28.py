class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        seen = set()

        def dfs(i):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for j in range(0, len(nums)):
                if j in seen:
                    continue
                
                curr.append(nums[j])
                seen.add(j)
                dfs(j + 1)
                
                curr.pop()
                seen.remove(j)

        dfs(0)
        return res