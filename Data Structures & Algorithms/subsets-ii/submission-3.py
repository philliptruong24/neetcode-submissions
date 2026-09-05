class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        curr = []
        
        def dfs(i):
            res.append(curr.copy())
            
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue

                curr.append(nums[j])
                dfs(j + 1)

                curr.pop()

        dfs(0)
        return res
        

        
