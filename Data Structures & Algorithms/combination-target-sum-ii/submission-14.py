class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        candidates.sort()
        
        def dfs(i, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if total > target or i == len(candidates):
                return
            
            curr.append(candidates[i])
            dfs(i + 1, total + candidates[i])

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            curr.pop()
            dfs(i + 1, total)
        
        dfs(0, 0)
        return res


